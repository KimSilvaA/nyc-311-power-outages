# NYC 311 Power Outage Complaints
![Screenshot of dashboard.](./Screenshot.png)
This is an end-to-end data analytics project focused on time series and geospatial analysis. The goal of this project was to practice implementing a data pipeline - from raw data extraction and transformation to interactive visualization. This pipeline:

- Extracts data from external APIs
- Loads raw data into a SQL database
- Performs transformation and aggregation
- Displays insights through an interactive, containerized dashboard 

## Objective
Analyze complaint trends in the NYC boroughs and boroughs over time.

## Datasets Used
This project currently uses the following datasets:
1. [311 Service Requests from 2020 to Present](https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2020-to-Present/erm2-nwe9/about_data) - provides information on submitted service requests
2. [2020 Neighborhood Tabulation Areas](https://data.cityofnewyork.us/City-Government/2020-Neighborhood-Tabulation-Areas-NTAs-/9nt8-h7nd/about_data) - contains geographic boundary polygons.

## Technologies 
### Data Extraction and Processing
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
This is the first working version of the dashboard. I would like to incorporate other kinds of data (<i>hint in code</i>) to perform other kinds of analysis.