import logging
from config import PipelineConfig
from pipeline import RetailETLPipeline


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def main():
    config = PipelineConfig(
        raw_file_path="data/raw/retail_sales.csv",
        cleaned_file_path="data/processed/cleaned_retail_sales.csv",
        summary_report_path="data/processed/sales_summary_by_region_category.csv"
    )

    pipeline = RetailETLPipeline(config)
    pipeline.run()


if __name__ == "__main__":
    main()