import os 
from dotenv import load_dotenv


# Load the .env file
load_dotenv()

COMPLAINTS_URL = "https://data.cityofnewyork.us/resource/erm2-nwe9.csv"

COMPLAINTS_COLUMN_NAMES = ['unique_key','created_date','closed_date','descriptor_2','incident_zip',
        'incident_address', 'street_name','city','resolution_description', 'status',
        'resolution_action_updated_date', 'community_board','borough','latitude','longitude']

DATABASE_URL = os.getenv("DATABASE_URL")

WEATHER_URL = "https://www.ncei.noaa.gov/cdo-web/api/v2/data"


# Tokens 
API_TOKEN = os.getenv("NYC_311_TOKEN")
WEATHER_TOKEN = os.getenv("WEATHER_API_TOKEN")
