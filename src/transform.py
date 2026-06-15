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

        df["delivery_days"] = (df["ship_date"] -df["order_date"]).dt.days
        
        invalid_delivery_days = df[df["delivery_days"]<0]

        if len(invalid_delivery_days)>0:
            logging.warning(f"Found{len(invalid_delivery_days)} rows with negative delivery days.")
        
        df["sales_category"] = pd.cut(
            df["sales"],
            bins = [0,100,500,float("inf")],
            labels = ["low","medium","high"]        
        )

        negative_sales = df[df["sales"]<0]

        if len(negative_sales)>0:
            logging.warning(f"Found {len(negative_sales)} rows with negative sales values.")


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
    