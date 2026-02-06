''' 
Functions to fetch data from NYC Open Data and Weather Data using APIs 
'''

import requests 
from config import *
from io import StringIO


def fetch_complaints(offset,limit=5):
    ''' 
    Fetches data from the 311 Service Requests from 2020 to Present Datasest
    '''

    url = COMPLAINTS_URL

    headers = {
        "X-App-Token": API_TOKEN,
        "Accept": "text/csv"
        }

    params = {
        "$where": "descriptor='POWER OUTAGE'",
        "$limit": limit,
        "$offset": offset
        }

    response = requests.get(url=url,headers=headers,params=params)

    return response


def check_response(response):
    ''' 
    The above function assumes the API Token is valid 
    This function checks whether that is true 
    '''
    try:
        response.raise_for_status()
    
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 403:
            error_type = "Invalid Token"
        else:
            error_type = "Error"
            
        print(error_type)
