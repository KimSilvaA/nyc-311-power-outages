import os 

COMPLAINTS_URL = "https://data.cityofnewyork.us/resource/erm2-nwe9.csv"

COMPLAINTS_COLUMN_NAMES = ['unique_key','created_date','closed_date','descriptor_2','incident_zip',
        'incident_address', 'street_name','city','resolution_description', 'status',
        'resolution_action_updated_date', 'community_board','borough','latitude','longitude']

COMPLAINTS_TOTAL_ROWS = 38342 # Actual number obtained using COUNT(*) function

API_TOKEN = os.getenv("NYC_311_TOKEN")

