import pandas as pd 
import geopandas as gpd
import json
import plotly.express as px 
from pathlib import Path 

ROOT = Path(__file__).resolve().parents[2]  # repo root, given src/analysis/...
csv_path = ROOT / "src" / "2020_Neighborhoods_Tabulation_Areas.csv"

crs="EPSG:4326"

def prepare_nta():
    
    # nta_df = pd.read_csv('../src/2020_Neighborhoods_Tabulation_Areas.csv')
    nta_df = pd.read_csv(csv_path)
    nta_df["the_geom"] = gpd.GeoSeries.from_wkt(nta_df["the_geom"])
    nta_gdf = gpd.GeoDataFrame(nta_df, geometry="the_geom", crs=crs)
    return nta_gdf 

def prepare_geodata(df,nta_gdf):
    gdf_complaints = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.longitude, df.latitude), crs=crs)
    gdf_merged = gpd.sjoin(gdf_complaints, nta_gdf, how="inner", predicate="within") 

    return gdf_merged

def subset_gdf(gdf_merged, start_date, end_date):
    gdf_merged_subset = gdf_merged[(gdf_merged.created_date.dt.date >= start_date) & (gdf_merged.created_date.dt.date < end_date)]
    return gdf_merged_subset

def count_complaints(gdf_merged_subset):
    counts = (
        gdf_merged_subset
        .groupby(["nta2020", "ntaname", "borough"], dropna=False)
        .agg(complaint_count=("unique_key", "size"))
        .reset_index()
        )
    return counts

def geoms_json(nta_gdf, counts):
    nta_counts_gdf = (
        nta_gdf[["nta2020", "ntaname", "the_geom"]]
        .merge(counts, on=["nta2020", "ntaname"], how="left")
        )

    nta_counts_gdf["complaint_count"] = nta_counts_gdf["complaint_count"].fillna(0).astype(int)
    geojson = json.loads(nta_counts_gdf.to_json())
    return geojson 

def create_heatmap(nta_counts_gdf, geojson, gdf_merged):
    fig = px.choropleth_map(
    nta_counts_gdf,
    geojson=geojson,
    locations="nta2020",
    featureidkey="properties.nta2020",
    color="complaint_count",
    color_continuous_scale="YlOrRd",
    map_style="carto-positron",
    zoom=9,
    center={
        "lat": gdf_merged.geometry.centroid.y.mean(),
        "lon": gdf_merged.geometry.centroid.x.mean(),
        },
    opacity=0.75,
    hover_name="ntaname",
    hover_data={
        "nta2020": False, 
        "complaint_count": True},
        )
    return fig 





