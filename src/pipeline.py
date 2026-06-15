import os
import logging
import pandas as pd
from config import PipelineConfig


class RetailETLPipeline:
    def __init__(self, config: PipelineConfig):
        self.config = config
        self.df = None
        self.cleaned_df = None

    def extract(self):
        try:
            logging.info("Starting extract step...")

            if not os.path.exists(self.config.raw_file_path):
                raise FileNotFoundError

            self.df = pd.read_csv(self.config.raw_file_path)

            logging.info("CSV file loaded successfully.")
            logging.info(
                f"Dataset loaded with {self.df.shape[0]} rows and {self.df.shape[1]} columns."
            )

        except FileNotFoundError:
            logging.error(f"File not found at path: {self.config.raw_file_path}")

        except Exception as e:
            logging.error(f"Unexpected error during extract step: {e}")

    def inspect(self):
        if self.df is None:
            logging.error("No data available for inspection.")
            return

        print("\n========== FIRST 5 ROWS ==========")
        print(self.df.head())

        print("\n========== DATASET SHAPE ==========")
        print(f"Rows: {self.df.shape[0]}")
        print(f"Columns: {self.df.shape[1]}")

        print("\n========== COLUMN NAMES ==========")
        print(self.df.columns.tolist())

        print("\n========== DATA TYPES ==========")
        print(self.df.dtypes)

        print("\n========== DATASET INFO ==========")
        self.df.info()

        print("\n========== MISSING VALUES ==========")
        print(self.df.isnull().sum())

        print("\n========== DUPLICATE ROWS ==========")
        print(self.df.duplicated().sum())

    def transform(self):
        try:
            if self.df is None:
                logging.error("No data available for transformation.")
                return

            logging.info("Starting transform step...")

            self.cleaned_df = self.df.copy()

            # Clean column names
            self.cleaned_df.columns = self.cleaned_df.columns.str.lower()
            self.cleaned_df.columns = self.cleaned_df.columns.str.replace(" ", "_")
            self.cleaned_df.columns = self.cleaned_df.columns.str.replace("-", "_")

            # Convert date columns
            self.cleaned_df["order_date"] = pd.to_datetime(
                self.cleaned_df["order_date"],
                format="%d/%m/%Y",
                errors="coerce"
            )

            self.cleaned_df["ship_date"] = pd.to_datetime(
                self.cleaned_df["ship_date"],
                format="%d/%m/%Y",
                errors="coerce"
            )

            # Create delivery_days column
            self.cleaned_df["delivery_days"] = (
                self.cleaned_df["ship_date"] - self.cleaned_df["order_date"]
            ).dt.days

            # Create sales_category column
            self.cleaned_df["sales_category"] = pd.cut(
                self.cleaned_df["sales"],
                bins=[0, 100, 500, float("inf")],
                labels=["Low", "Medium", "High"]
            )

            # Handle missing postal code values
            self.cleaned_df["postal_code"] = self.cleaned_df["postal_code"].fillna("Unknown")

            logging.info("Transform step completed successfully.")

        except KeyError as e:
            logging.error(f"Column not found during transform step: {e}")

        except Exception as e:
            logging.error(f"Unexpected error during transform step: {e}")

    def validate(self):
        if self.cleaned_df is None:
            logging.error("No cleaned data available for validation.")
            return

        logging.info("Starting data validation step...")

        invalid_delivery_days = self.cleaned_df[self.cleaned_df["delivery_days"] < 0]

        if len(invalid_delivery_days) > 0:
            logging.warning(
                f"Found {len(invalid_delivery_days)} rows with negative delivery days."
            )

        negative_sales = self.cleaned_df[self.cleaned_df["sales"] < 0]

        if len(negative_sales) > 0:
            logging.warning(
                f"Found {len(negative_sales)} rows with negative sales values."
            )

        missing_order_dates = self.cleaned_df["order_date"].isnull().sum()
        missing_ship_dates = self.cleaned_df["ship_date"].isnull().sum()

        if missing_order_dates > 0:
            logging.warning(f"Found {missing_order_dates} missing/invalid order dates.")

        if missing_ship_dates > 0:
            logging.warning(f"Found {missing_ship_dates} missing/invalid ship dates.")

        logging.info("Data validation step completed.")

    def load(self):
        try:
            if self.cleaned_df is None:
                logging.error("No cleaned data available to load.")
                return

            logging.info("Starting load step...")

            output_folder = os.path.dirname(self.config.cleaned_file_path)

            if not os.path.exists(output_folder):
                os.makedirs(output_folder)
                logging.info(f"Created output folder: {output_folder}")

            self.cleaned_df.to_csv(self.config.cleaned_file_path, index=False)

            logging.info(
                f"Cleaned data saved successfully at: {self.config.cleaned_file_path}"
            )

        except Exception as e:
            logging.error(f"Unexpected error during load step: {e}")

    def generate_report(self):
        try:
            if self.cleaned_df is None:
                logging.error("No cleaned data available for report generation.")
                return

            logging.info("Starting summary report generation...")

            summary = (
                self.cleaned_df
                .groupby(["region", "category"])["sales"]
                .sum()
                .reset_index()
            )

            output_folder = os.path.dirname(self.config.summary_report_path)

            if not os.path.exists(output_folder):
                os.makedirs(output_folder)

            summary.to_csv(self.config.summary_report_path, index=False)

            logging.info(
                f"Summary report saved successfully at: {self.config.summary_report_path}"
            )

        except KeyError as e:
            logging.error(f"Column not found during report generation: {e}")

        except Exception as e:
            logging.error(f"Unexpected error during report generation: {e}")

    def run(self):
        logging.info("Pipeline started.")

        self.extract()
        self.inspect()
        self.transform()
        self.validate()
        self.load()
        self.generate_report()

        logging.info("Pipeline completed.")