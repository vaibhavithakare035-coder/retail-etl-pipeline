import os

def load_data(df,output_path):
    print("Starting load step... ")

    output_folder = os.path.dirname(output_path)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    df.to_csv(output_path,index=False)

    print(f"Cleaned date saved successfully at: {output_path}")
    