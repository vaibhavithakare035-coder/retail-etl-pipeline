import logging
import pandas as pd


def transform_data(df):
    try:
        logging.info("Starting transform step...")

        # Clean column names
        df.columns = df.columns.str.lower()
        df.columns = df.columns.str.replace(" ", "_")
        df.columns = df.columns.str.replace("-", "_")

        # Convert date columns
        df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
        df["ship_date"] = pd.to_datetime(df["ship_date"], errors="coerce")

        # Handle missing postal code values
        df["postal_code"] = df["postal_code"].fillna("Unknown")

        logging.info("Transform step completed successfully.")
        return df

    except KeyError as e:
        logging.error(f"Column not found during transform step: {e}")
        return None

    except Exception as e:
        logging.error(f"Unexpected error during transform step: {e}")
        return None