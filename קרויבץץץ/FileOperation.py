import numpy as np
import pandas as pd
from Exceptions import Exceptions

exception_handler = Exceptions()
class FileOperation:

    def read_excel(self, file_path: str):
        try:
            data = pd.read_csv(file_path)  # Use pd.read_csv() to read CSV files
            return data
        except Exception as e:
            exception_handler.print_exception(f"Error reading CSV file: {e}")
            return None

    def save_to_excel(self, data, file_name: str):
        try:
            if isinstance(data, pd.DataFrame):
                data.to_csv(file_name, index=False)
                print(f"Data saved to {file_name} successfully.")
                return True
            else:
                print("Invalid data type. Please provide a Pandas DataFrame.")
                return False
        except Exception as e:
            exception_handler.print_exception(f"Error saving data to Excel file: {e}")
            return False
