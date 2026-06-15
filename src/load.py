import os
import logging 


def load_data(df,output_path):
    try:
        logging.info("Starting load step...")
        output_folder = os.path.dirname(output_path)
       
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
            logging.info(f"Created output folder:{output_folder}")

        df.to_csv(output_path,index=False)

        logging.info(f"Cleaned date saved successfully at: {output_path}")

    except Exception as e:
        logging.error(f"Unexpected error during load step: {e}")
    



    