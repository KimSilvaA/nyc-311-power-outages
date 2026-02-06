from config import *
import pandas as pd 
from io import StringIO
from fetch_data import fetch_complaints
from sqlalchemy import create_engine

''' 
Function to store pandas DataFrames (csv formats) to SQL 
'''
engine = create_engine("sqlite:///power_outages.db")

def save_to_sql(df, table_name, engine):
    df.to_sql(table_name, con=engine, if_exists="append", index=False)
