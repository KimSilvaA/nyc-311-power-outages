from etl.fetch_utils import fetch_weather

response = fetch_weather('2020-01-01', '2020-01-02')
print(response.text)