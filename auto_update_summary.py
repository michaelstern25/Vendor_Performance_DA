import os
import pandas as pd
import logging
from sqlalchemy import create_engine
from ingestion_db import ingest_db
from get_vendor_summary import create_ven_summary, clean_data

# Setup logging
logging.basicConfig(
    filename="logs/auto_update_summary.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Create database engine
engine = create_engine('sqlite:///inventory.db')

# Step 1: Automatically detect and load all CSV files into DB
def auto_ingest_csvs():
    logging.info("🔄 Starting ingestion of CSV files...")
    for file in os.listdir('data'):
        if file.endswith('.csv'):
            table_name = file.replace('.csv', '')
            file_path = os.path.join('data', file)
            df = pd.read_csv(file_path)
            ingest_db(df, table_name, engine)
            logging.info(f"✅ Appended {file} to table {table_name}")

# Step 2: Generate updated vendor summary
def update_summary():
    logging.info("📊 Generating updated vendor summary...")
    conn = engine.connect()
    summary_df = create_ven_summary(conn)
    clean_df = clean_data(summary_df)
    ingest_db(clean_df, 'vendor_sales_summary', engine)
    logging.info("✅ Vendor sales summary updated and saved to DB.")

if __name__ == '__main__':
    auto_ingest_csvs()
    update_summary()
    logging.info("✅✅ ALL DONE!")

# ingestion_db.py (ensure this is updated)
# def ingest_db(df, table_name, engine):
#     '''Append instead of replace'''
#     df.to_sql(table_name, con=engine, if_exists='append', index=False)
