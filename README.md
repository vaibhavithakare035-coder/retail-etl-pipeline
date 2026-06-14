# Retail ETL Pipeline

This is a beginner-friendly data engineering project built using Python and Pandas.

The goal of this project is to build an ETL pipeline for retail sales data.

## Current Progress

Currently completed:

- Extract stage
- Read raw CSV file using Pandas
- Validate whether the file exists
- Handle file reading errors using exception handling
- Add logging for success and error messages
- Inspect dataset shape, columns, data types, missing values, and duplicate rows

## Project Structure

```text
retail etl pipeline/
├── data/
│   ├── raw/
│   └── processed/
├── src/
│   └── extract.py
├── .gitignore
├── requirements.txt
└── README.md