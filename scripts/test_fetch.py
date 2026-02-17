from config import *
from etl.fetch_utils import fetch_complaints
import pandas as pd 
from io import StringIO

response = fetch_complaints(limit=5)

df = pd.read_csv(StringIO(response.text), usecols = COMPLAINTS_COLUMN_NAMES)

print(df.head())



