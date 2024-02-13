import pandas as pd


class FileOperation:
    def read_csv(self, file_path: str):
        """
        Read data from a CSV file located at the specified file path.

        Parameters:
        file_path (str): Path to the CSV file.

        Returns:
        DataFrame: Data read from the CSV file.
        """
        try:
            data = pd.read_csv(file_path)
            return data
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
            return None
        except Exception as e:
            print(f"An error occurred while reading the CSV file: {e}")
            return None

    def save_to_csv(self, data, file_name: str):
        """
        Save the provided data to a new CSV file with the given file name.
        If the file already exists, it will be overwritten.

        Parameters:
        data (DataFrame): Data to be saved to the CSV file.
        file_name (str): Name of the CSV file to be saved.
        """
        try:
            data.to_csv(file_name, index=False)
            print(f"Data successfully saved to '{file_name}'.")
        except Exception as e:
            print(f"An error occurred while saving data to CSV file: {e}")
