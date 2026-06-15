# Retail ETL Pipeline

This is an object-oriented data engineering project built using Python and Pandas.

The goal of this project is to build an ETL pipeline for retail sales data. The pipeline reads raw retail sales data, cleans and transforms it, validates data quality, saves cleaned output, and generates a summary report.

## OOP Design

This project uses an object-oriented design.

* `PipelineConfig` stores file paths for input and output files.
* `RetailETLPipeline` contains the complete ETL logic.
* The pipeline class includes methods for extract, inspect, transform, validate, load, report generation, and running the full pipeline.
* `main.py` creates a pipeline object and runs the complete workflow.

## Current Progress

Completed:

### Extract Stage

* Reads raw CSV file using Pandas
* Validates whether the file exists
* Handles file reading errors using exception handling
* Adds logging for success and error messages
* Inspects dataset shape, columns, data types, missing values, and duplicate rows

### Transform Stage

* Cleans column names
* Converts date columns to datetime format
* Handles missing postal code values
* Creates `delivery_days` column from order date and ship date
* Creates `sales_category` column based on sales amount

### Validation Stage

* Checks for negative delivery days
* Checks for negative sales values
* Checks for missing or invalid order dates
* Checks for missing or invalid ship dates

### Load Stage

* Saves cleaned data into `data/processed/cleaned_retail_sales.csv`

### Report Generation

* Creates a sales summary report by region and category
* Saves the report as `data/processed/sales_summary_by_region_category.csv`

### Main Pipeline Runner

* Runs Extract, Inspect, Transform, Validate, Load, and Report stages together using `src/main.py`

## Project Structure

```text
retail etl pipeline/
├── data/
│   ├── raw/
│   │   └── retail_sales.csv
│   └── processed/
│       ├── cleaned_retail_sales.csv
│       └── sales_summary_by_region_category.csv
├── src/
│   ├── config.py
│   ├── pipeline.py
│   ├── main.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── report.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Dataset

The raw dataset should be placed inside:
data/raw/

Example:
data/raw/retail_sales.csv

CSV files are not pushed to GitHub because they may be large or private.

## Installation

Install the required Python libraries:
pip install -r requirements.txt

## Run Full OOP ETL Pipeline

From the main project folder, run:
python src/main.py

This command runs the complete pipeline:
Extract → Inspect → Transform → Validate → Load → Report

## Output Files

After running the pipeline, these files are created locally:
data/processed/cleaned_retail_sales.csv
data/processed/sales_summary_by_region_category.csv

These files are not pushed to GitHub because processed CSV files are ignored using `.gitignore`.

## Technologies Used

* Python
* Pandas
* Object-Oriented Programming
* Logging
* Exception Handling
* Git
* GitHub

