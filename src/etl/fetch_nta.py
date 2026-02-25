from fetch_utils import fetch_nta
import pandas as pd
from io import StringIO

''' 
Logging not used because this data is much easier to handle 
'''

def main():
    response = fetch_nta()
    df = pd.read_csv(StringIO(response.text))
    if df["nta2020"].nunique() == 262:
        print("Success!")
        df.to_csv("2020_Neighborhoods_Tabulation_Areas.csv")
    else:
        print("Non-unique NTA2020 values found")

if __name__ == "__main__":
    main()

