# Retail ETL Pipeline

This is a beginner-friendly data engineering project built using Python and Pandas.

The goal of this project is to build an ETL pipeline for retail sales data.

## Current Progress

Completed:

- Extract stage
  - Reads raw CSV file using Pandas
  - Validates whether the file exists
  - Handles file reading errors using exception handling
  - Adds logging for success and error messages
  - Inspects dataset shape, columns, data types, missing values, and duplicate rows

- Transform stage
  - Cleans column names
  - Converts date columns to datetime format
  - Handles missing postal code values
  - Creates `delivery_days` column from order date and ship date
  - Creates `sales_category` column based on sales amount

- Load stage
  - Saves cleaned data into `data/processed/cleaned_retail_sales.csv`

- Main pipeline runner
  - Runs Extract, Transform, and Load together using `src/main.py`

- Run Full ETL Pipeline
From the main project folder, run:
python src/main.py
This command runs the complete ETL pipeline:
Extract → Transform → Load
The cleaned output file will be created at:
data/processed/cleaned_retail_sales.csv

- Report generation
  - Creates a sales summary report by region and category
  - Saves the report as `data/processed/sales_summary_by_region_category.csv`

  - Output Files
    After running the pipeline, these files are created locally:
    ```text
    data/processed/cleaned_retail_sales.csv
    data/processed/sales_summary_by_region_category.csv


## Project Structure

retail etl pipeline/
├── data/
│   ├── raw/
│   └── processed/
├── src/
│   └── extract.py
├── .gitignore
├── requirements.txt
└── README.md