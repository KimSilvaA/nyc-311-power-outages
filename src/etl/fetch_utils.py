''' 
Functions to fetch data from NYC Open Data and Weather Data using APIs 
'''

import requests 
from config import * 
from io import StringIO
import pandas as pd 
import re


def count_instances():
    ''' 
    Returns the number of row entries where the complaint was a power outage
    '''
    url = COMPLAINTS_URL

    headers = {
        "X-App-Token": API_TOKEN,
        "Accept": "text/csv"
    }

    params = {
        "$select": "count(*) AS count",
        "$where": "descriptor='POWER OUTAGE'",
    }        
    response = requests.get(url=url, headers=headers, params=params)

    if response.status_code != 200:
        raise RuntimeError(f"Error: Status code {response.status_code}")
    
    total_rows = response.text
    count = int(re.search(r"\d+", total_rows).group())

    return count



def build_params(limit=5, **kwargs):
    ''' 
    Returns the parameters needed to send the HTTP GET request
    for the complaints data 
    Input
    ------
    limit (int): maximum num of rows returned in one request
    date (ISO 8601): earliest datetime to look for
    id (int): unique_key value 
    '''

    params = {
        "$where": "descriptor='POWER OUTAGE'",
        "$limit": limit,
        "$offset": 0,
        "$order": "created_date ASC, unique_key ASC"
    }

    
    last_date = kwargs.get('date')
    last_id = kwargs.get('id')

    if last_date is not None:
        where = f"descriptor = 'POWER OUTAGE' AND ((created_date > '{last_date}') OR (created_date = '{last_date}' AND unique_key > '{last_id}'))"
        params["$where"] = where


    return params 



def fetch_complaints(limit=5, **kwargs):
    
    url = COMPLAINTS_URL

    headers = {
        "X-App-Token": API_TOKEN,
        "Accept": "text/csv"
    }

    params = build_params(limit=limit, **kwargs)
        
    response = requests.get(url=url, headers=headers, params=params)

    if response.status_code != 200:
        raise RuntimeError(f"Error: Status code {response.status_code}")
    
    return response

def fetch_weather(start_date, end_date):
    ''' 
    Fetches daily weather summaries of NYC in date range
    start_date and end_date must be in ISO 8601 format (YYYY-MM-DD)
    '''
    url = WEATHER_URL
    headers = {
        "token": WEATHER_TOKEN,
        }
    params = {
        "datasetid": "GHCND",
        "startdate": start_date,
        "enddate": end_date,
        "locationid": "CITY:US360019",
        "datatypeid": ["TMAX", "TMIN"],
        "units": "standard",
        "stationid": "GHCND:USW00094728",
        'limit': 100
    }
    response = requests.get(url=url, headers=headers, params=params)

    if response.status_code != 200:
        print(response.text)
        raise RuntimeError(f"Error: Status code {response.status_code}")

    return response 

def check_timedelta(start_date, end_date):
    ''' 
    Returns True if start_date and end_date are less than a year apart
    start_date and end_date must be in datetime format
    '''
    diff = (end_date - start_date).days 
    return diff < 365 


def fetch_nta():
    ''' 
    Fetches data from the Neighborhoods Tabulation Area Dataset
    '''
    url = NTA_URL 

    headers = {
        "X-App-Token": API_TOKEN,
        "Accept": "text/csv"
    }

    params = {
    "$limit": 262,
    "$offset": 0,
    "$order": "nta2020"
    }

    response = requests.get(url=url, headers=headers, params=params)
    if response.status_code != 200:
        print(response.text)
        raise RuntimeError(f"Error: Status code {response.status_code}")

    return response 

