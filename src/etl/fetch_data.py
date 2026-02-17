from fetch_utils import *
from store_sql import *
import logging
from datetime import datetime

logging.basicConfig(filename='logs/api.log', 
                    encoding='utf-8',
                    level=logging.DEBUG,
                    format='%(asctime)s %(message)s')

logger = logging.getLogger(__name__)



def main():
    engine = create_engine("sqlite:///power_outages.db")
    last_date = None
    last_id = None
    batch = 1 
    total_fetched_rows = 0
    limit = 1000

    logger.info(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} Starting NYC Open Data fetch")
    
    while True:
        try:
        # Fetch data 
            response = fetch_complaints(limit=limit, date=last_date, id=last_id)
            df_chunk = pd.read_csv(StringIO(response.text), usecols = COMPLAINTS_COLUMN_NAMES)

            rows = len(df_chunk)

            # Check if done 
            if rows == 0:
                logger.info("No more rows to fetch - Data retrieval complete")
                break

            # Get first and last records of chunk for logging
            first_date = df_chunk['created_date'].iloc[0]
            first_id = df_chunk['unique_key'].iloc[0]
            last_date = df_chunk['created_date'].iloc[-1]
            last_id = df_chunk['unique_key'].iloc[-1]

            logger.info(f"Batch {batch}: {rows} rows | {first_date}/ID({first_id}) to {last_date}/ID{last_id} ")
            
            batch+=1
            total_fetched_rows+=rows

            df_chunk.to_sql("POWER_OUTAGES", con=engine, if_exists="append", index=False)

            del(df_chunk)
            del(response)

            # Check for last batch
            if rows < limit:
                logger.info("Final batch received - Data retrieval complete")
                break
        
        except Exception as e:
            logger.error(f"ERROR at Batch {batch}, Cursor: {last_date}/ID({last_id}) - {str(e)}")


    logger.info(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Fetch complete")
    logger.info(f"Total batches: {batch - 1}")
    logger.info(f"Total rows fetched: {total_fetched_rows}")


# if __name__ == "__main__":
#     main() 