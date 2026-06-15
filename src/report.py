import os
import pandas as pd


def generate_summary_report(input_path, output_path):
    print("Starting summary report generation...")

    df = pd.read_csv(input_path)

    summary = df.groupby(["region","category"])["sales"].sum().reset_index()

    output_folder = os.path.dirname(output_path)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    summary.to_csv(output_path, index=False)

    print(f"Summary report saved successfully at: {output_path}") 