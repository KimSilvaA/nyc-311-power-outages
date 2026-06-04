import sys
sys.path.insert(0, 'src/etl')

from store_sql import get_last_record, engine

result = get_last_record(engine)
print("Last record:", result)
