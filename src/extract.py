import os 
import logging 
import pandas as pd

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s" 
)

def extract_data(file_path):
    try:
        logging.info("Strating extract step...")

        if not os.path.exists(file_path):
            raise FileNotFoundError
        
        df =  pd.read_csv(file_path)

        logging.info("CSV file loaded successfully.")
        logging.info(f"Dataset loaded with {df.shape[0]} rows and {df.shape[1]} columns")
        return df
    
    except FileNotFoundError:
        logging.error(f"Error: File not found at path: {file_path}")
        return None
    
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return None

def inspect_data(df):
    print("\n========== FIRST 5 ROWS ==========")
    print(df.head())

    print("\n========== DATASET SHAPE ==========")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")

    print("\n========== COLUMN NAMES ==========")
    print(df.columns.tolist())

    print("\n========== DATA TYPES ==========")
    print(df.dtypes)

    print("\n========== DATASET INFO ==========")
    df.info()

    print("\n========== MISSING VALUES ==========")
    print(df.isnull().sum())

    print("\n========== DUPLICATE ROWS ==========")
    print(df.duplicated().sum())

if __name__ == "__main__":
    file_path = "data/raw/retail_sales.csv"

    df = extract_data(file_path)

    if df is not None:
        inspect_data(df)
