import pandas as pd
import os
from sqlalchemy import create_engine
import time
import logging

logging.basicConfig(
    filename="logs/ingestion_db.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

engine = create_engine('sqlite:///inventory.db')

def ingest_db(df, table_name, engine):
    '''This function ingests the dataframe into a database table'''
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)

def load_raw_data():
    '''This function loads CSV, Excel, and JSON files as DataFrame and ingests them into DB'''
    start = time.time()
    
    for file in os.listdir('data'):
        file_path = os.path.join('data', file)
        if file.endswith('.csv'):
            df = pd.read_csv(file_path)
            table_name = file[:-4]
        elif file.endswith('.xlsx') or file.endswith('.xls'):
            df = pd.read_excel(file_path)
            table_name = file[:-5]
        elif file.endswith('.json'):
            df = pd.read_json(file_path)
            table_name = file[:-5]
        else:
            continue  # skip unsupported file types
        
        logging.info(f'Ingesting {file} into DB...')
        ingest_db(df, table_name, engine)
    
    end = time.time()
    total_time = (end - start)/60
    logging.info('-----------Ingestion Complete-----------')
    logging.info(f'Total Time Taken: {total_time} minutes')

if __name__ == '__main__':
    load_raw_data()
