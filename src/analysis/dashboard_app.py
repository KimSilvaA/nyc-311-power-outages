from load_data import load_dataframes
from geospatial import *
import streamlit as st


df = load_dataframes()
nta_gdf = prepare_nta()
gdf_merged = prepare_geodata(df,nta_gdf)

st.set_page_config(layout="wide")
st.title("NYC 311 Power Outage Complaints")


earliest_date = df.created_date.min()
latest_date = df.created_date.max()

d = st.date_input(
    "Select the date range (must be different dates!)",
    (earliest_date, latest_date),
    earliest_date,
    latest_date,
    format="MM.DD.YYYY",
    )


if st.button("Let's Analyze!") and len(d) ==2:
    with st.spinner("Loading!", show_time=True):
        start_date = d[0]
        end_date = d[1]

        gdf_merged_subset = subset_gdf(gdf_merged, start_date, end_date)

        counts = count_complaints(gdf_merged_subset)
        top_neighborhood = counts.loc[counts['complaint_count'].idxmax(),'ntaname']
        borough_count = counts.groupby('borough')['complaint_count']
        top_borough = borough_count.sum().idxmax()
        resolve_avg = gdf_merged_subset[gdf_merged_subset['status'].eq('Closed')].resolve_time_hours.mean()
        units = 'hours'
        if resolve_avg > 24:
            resolve_avg = round(resolve_avg/24)
            units = 'days'


        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Total number of complaints", value=len(gdf_merged_subset))
        col2.metric("Most affected borough", value=top_borough)
        col3.metric("Most affected neighborhood", value=top_neighborhood, width='content')
        col4.metric(f"Average Resolution Time ({units})", value=round(resolve_avg))

        geojson = geoms_json(nta_gdf, counts)

        nta_counts_gdf = (
            nta_gdf[["nta2020", "ntaname", "the_geom"]]
            .merge(counts, on=["nta2020", "ntaname"], how="left")
        )

        fig = create_heatmap(nta_counts_gdf, geojson, gdf_merged_subset)

        fig.update_traces(marker_line_width=0.6, marker_line_color="black")
        fig.update_layout(height=800)


        gdf_merged_subset['day'] = gdf_merged_subset['created_date'].dt.date

        counts_by_date = gdf_merged_subset.groupby('day').size().reset_index(name='count')
        counts_by_date = counts_by_date.set_index('day').asfreq('D', fill_value=0).reset_index()

        fig1 = px.line(counts_by_date, x='day', y="count", title="Complaints Over Time")
        fig2 = px.histogram(gdf_merged_subset, x="borough")

        col1, col2= st.columns(2)
        
        with col1:
            st.plotly_chart(fig, theme="streamlit", width="stretch")
        with col2:
            st.plotly_chart(fig1, theme="streamlit", width="content",height="content")
            subcol, = st.columns(1)
            with subcol:
                st.plotly_chart(fig2, theme="streamlit", width="content",height="content")

    