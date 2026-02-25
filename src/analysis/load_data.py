import pandas as pd 
import sqlalchemy as sa 
import numpy as np

def db_to_df():
    # Create and connect to engine 
    engine = sa.create_engine("sqlite:///../power_outages.db")
    connection = engine.connect()

    # Create Resolve Time column 
    q = sa.text("""SELECT * FROM POWER_OUTAGES""")

    # Read to pandas dataframe 
    df = pd.read_sql(q, connection)

    # Close connection to database 
    connection.close()
    engine.dispose() 

    return df 

def prepare_df(df):
    # Format columns 
    df['created_date'] = pd.to_datetime(df['created_date'], utc=False)
    df['closed_date'] = pd.to_datetime(df['closed_date'], utc=False)
    df['resolution_action_updated_date'] = pd.to_datetime(df['resolution_action_updated_date'], utc=False)
    df['resolve_time_hours'] = (df['closed_date'] - df['created_date']).dt.total_seconds() / 3600
    df['resolve_time_hours'] = np.floor(pd.to_numeric(df['resolve_time_hours'], errors='coerce')).astype('Int64')
    df['incident_zip'] = df['incident_zip'].astype('Int64') 
    df["incident_address"] = (df["incident_address"].str.replace(r"\s+", " ", regex=True))

    # Filter duplicates and null geospatial values 
    df = df[~df.resolution_description.str.contains('duplicate',na=False)] #  > 2000 rows
    df = df[~df['latitude'].isnull()] # 2 rows containing NAN values 
    df = df[~df['longitude'].isnull()] # ""
    return df 


def load_dataframes():
    raw_df = db_to_df()
    return prepare_df(raw_df)
    

