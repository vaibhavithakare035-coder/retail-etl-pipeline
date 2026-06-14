from extract import extract_data, inspect_data
from transform import transform_data
from load import load_data


def main():
    print("Pipeline started")

    raw_file_path = "data/raw/retail_sales.csv"
    output_file_path = "data/processed/cleaned_retail_sales.csv"

    df = extract_data(raw_file_path)

    if df is not None:
        inspect_data(df)

        cleaned_df = transform_data(df)

        if cleaned_df is not None:
            load_data(cleaned_df, output_file_path)

    print("Pipeline completed")


if __name__ == "__main__":
    main()