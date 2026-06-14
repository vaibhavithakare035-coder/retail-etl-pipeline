import pandas as pd

def transform_data(df):
    print("Starting transfrom step")
    
    df.columns = df.columns.str.lower()
    df.columns = df.columns.str.replace(" ","_")
    df.columns = df.columns.str.replcae("-","_")


    df["order_date"] = pd.to_datetime(df["order_date"],errors="coerce")
    df["ship_date"] = pd.to_datetime(df["ship_date"],errors="coerce")

    df["postal_code"] = df["postal_code"].fillna("Unknown")

    print("Transform step completed successfully")

    return df 