from fetch_utils import fetch_weather, check_timedelta
import pandas as pd
import os
import sqlalchemy as sa 
from datetime import timedelta

# I will use this one day!


def main():
    engine = sa.create_engine("sqlite:///../power_outages.db")
    connection = engine.connect()
    last_date_q = connection.execute(sa.text("""SELECT created_date FROM POWER_OUTAGES ORDER BY created_date DESC LIMIT 1;
    """))
    last_date = last_date_q.scalar() 
    last_date = pd.to_datetime(last_date)

    connection.close()
    engine.dispose() 
    
    weather = pd.DataFrame()

    start_date = pd.to_datetime('2020-01-01 00:00:00')
    while start_date <= last_date:
        # check whether dates are within a year 
        if not check_timedelta(start_date, last_date):
            end_date = start_date + timedelta(days=365)

        else:
            end_date = last_date 

        response = fetch_weather(str(start_date.date()), str(end_date.date())) 
        data = response.json()

        # Filter out header rows from the raw data
        results = [row for row in data['results'] if row.get('date') != 'date']

        df = pd.DataFrame(results) 
        df["date"] = pd.to_datetime(df['date'], utc=False)
        weather = pd.concat([weather, df])
        weather = weather.drop_duplicates()
        start_date = weather["date"].iloc[len(weather)-1]  

    weather.to_csv('weather.csv', mode='w', index=False)  


if __name__ == "__main__":
    main()

