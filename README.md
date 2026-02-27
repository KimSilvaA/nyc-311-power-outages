# NYC 311 Power Outage Complaints
![Screenshot of dashboard.](./Screenshot.png)
This is an end-to-end data analytics project focused on time series and geospatial analysis. The goal of this project was to practice implementing a data pipeline - from raw data extraction and transformation to interactive visualization. This pipeline:

- Extracts data from external APIs
- Loads raw data into a SQL database
- Performs transformation and aggregation
- Displays insights through an interactive, containerized dashboard 

## Objective
Analyze complaint trends in the NYC boroughs and neighborhoods over time.

## Background and Motivation
Aside from wanting to learn new skills, I chose to analyze power outage complaints out of personal curiosity and observation. Below summarizes the results of a quick Google search.

<p>

Blackouts are increasing in both frequency and severity—by as much as 20% annually since 2019—particularly along the East Coast among other areas. <sup>[1](https://stories.tamu.edu/news/2025/08/14/texas-am-researchers-map-americas-power-outage-hot-spots-using-ai/)</sup> The Department of Energy warns that outages could grow dramatically, potentially by up to 100 times by 
2030. <sup>[2](https://www.energy.gov/articles/department-energy-releases-report-evaluating-us-grid-reliability-and-security)</sup> 


Because outages spike during extreme weather, worsening climate conditions are likely to amplify the problem. Beyond disruption, blackouts carry real health consequences, as seen in the rise in hospitalizations during the 2003 New York City blackout. <sup>[3](https://a816-dohbesp.nyc.gov/IndicatorPublic/data-stories/poweroutages/)</sup>

<p>

Therefore, the motivation of this project was to identify spatial and temporal trends in power outage complaints in NYC. Here are some of the questions I had in mind:
1. Is there a trend in annual complaint frequency over the six-year period?
2. Are there neighborhoods that are affected more throughout the year? 
3. Are there more complaints in the summer or winter months? 




## Datasets Used
This project currently uses the following datasets:
1. [311 Service Requests from 2020 to Present](https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2020-to-Present/erm2-nwe9/about_data) - provides information on submitted service requests
2. [2020 Neighborhood Tabulation Areas](https://data.cityofnewyork.us/City-Government/2020-Neighborhood-Tabulation-Areas-NTAs-/9nt8-h7nd/about_data) - contains geographic boundary polygons.

## Technologies 
### Data Extraction and Processing
<b> Data Extraction and Processing </b>
- Python (pandas, geopandas, numpy, sqlalchemy)
### Visualization 
- Streamlit
- Plotly
### Infrastructure
- Docker (for dashboard deployment)

## Setup
1. Git clone the repo
2. Build docker image <br>
` docker build -t nyc-311 . `
3. Run the container <br>
`docker run -p 8501:8501 nyc-311` </br>

## Future Improvements
This is the first working version of the dashboard. I would like to incorporate other kinds of data (<i>hint in code</i>) to perform different types of analysis. 
