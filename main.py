from fetch_data import *
from store_sql import *


def main():
    total_rows = COMPLAINTS_TOTAL_ROWS 

    offset = 0
    engine = create_engine("sqlite:///power_outages.db")
    while offset < total_rows:
        response = fetch_complaints(offset,limit=1000)
        check_response(response)
        df_chunk = pd.read_csv(
            StringIO(response.text),
            usecols = COMPLAINTS_COLUMN_NAMES
            )
        df_chunk.to_sql("POWER_OUTAGES", con=engine, if_exists="append", index=False)
        del(df_chunk)
        offset+=1000 

    del(response)

if __name__ == "__main__":
    main() 