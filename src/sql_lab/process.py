import os
import logging
import pandas as pd
from sqlalchemy import create_engine, text

DBHOST = os.environ.get("DBHOST")
DBUSER = os.environ.get("DBUSER")
DBPASS = os.environ.get("DBPASS")
DBNAME = os.environ.get("DBNAME")
CSV_FILE = "MOCK_DATA.csv"
TABLE = "mock"

def read_data(filename):
    """
    Load CSV file into pandas dataframe
    """
    logging.info(f"Loading...")
    df = pd.read_csv(filename)
    logging.info(f"Successfuly loaded {len(df)} rows.")
    return df

def clean_data(data):
    """
    Drop missing rows to prepare for upload
    """
    logging.info(f"Cleaning data...")
    initial_length = len(data) #using for logging
    clean_df = data.dropna()
    logging.info(f"Successfuly removed {initial_length - len(clean_df)} rows.")
    return clean_df

def load_data(data, table):
    """
    Bulk Upload of Data
    """ #using sql alchemy
    url = f"mysql+mysqlconnector://{DBUSER}:{DBPASS}@{DBHOST}:3306/{DBNAME}" #connection url
    engine = create_engine(url)
    logging.info("Database engine created. Starting upload...")
    try:
        data.to_sql(table, con=engine, if_exists='replace', index=False)
        with engine.connect() as conn:
            query = f"SELECT COUNT(*) FROM {table}"
            count = conn.execute(text(query)).scalar()
            logging.info(f"Uploaded {count} rows to {DBNAME}.{table}")
    except Exception as e:
        print(f"Upload failed: {e}")
        raise
    finally:
        engine.dispose() #closing out

def main(f):
    try:
        df = read_data(f)
        clean_df = clean_data(df)
        load_data(clean_df, table="mock")
    except Exception as e:
        print(f'Failure: {e}')

if __name__ == "__main__":
    main(CSV_FILE)
    
    
