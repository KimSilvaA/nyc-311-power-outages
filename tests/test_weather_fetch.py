from etl.fetch_utils import fetch_weather
from io import StringIO
import pandas as pd 

response = fetch_weather('2020-01-13', '2021-01-01')
data = response.json()


df = pd.DataFrame(data['results']) 
# df = df[df["date"] != "date"]
print(df.head)

# df.to_csv('weather.csv',mode='a',index=False)

