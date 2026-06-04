import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from config import *
import pandas as pd 
from io import StringIO
from fetch_utils import fetch_complaints
from sqlalchemy import create_engine, inspect
import sqlalchemy as sa

''' 
Function to store pandas DataFrames (csv formats) to SQL 
'''
# Database path: always look in src/ directory (one level up from this file)
db_path = os.path.join(os.path.dirname(__file__), "..", "power_outages.db")
engine = create_engine(f"sqlite:///{os.path.abspath(db_path)}")

def save_to_sql(df, table_name, engine):
    df.to_sql(table_name, con=engine, if_exists="append", index=False)

def get_last_record(engine, db_table=DB_TABLE):
    """
    Get the last record inserted (by date and ID) to use as cursor.
    
    Returns: dict with 'created_date' and 'unique_key', or None if table empty
    """
    try:
        q = sa.text(f"""SELECT created_date, unique_key 
                     FROM {db_table} 
                     ORDER BY created_date DESC, unique_key DESC 
                     LIMIT 1""")
        
        with engine.connect() as conn:
            result = conn.execute(q)
            row = result.fetchone()
            if row:
                return {'created_date': row[0], 'unique_key': row[1]}
            return None
        
    except Exception as e:
        raise RuntimeError(f"Error getting last record: {str(e)}")
