import unittest
import pandas as pd
from unittest.mock import patch
from FileOperation import FileOperation


class TestFileOperation(unittest.TestCase):
    @patch('builtins.print')
    def test_read_csv_file_not_found(self, mock_print):
        file_op = FileOperation()
        data = file_op.read_csv("nonexistent.csv")
        self.assertIsNone(data)
        mock_print.assert_called_once_with("File 'nonexistent.csv' not found.")

    def test_read_csv_exception(self):
        file_op = FileOperation()
        with patch('pandas.read_csv') as mock_read_csv:
            mock_read_csv.side_effect = Exception("Test exception")
            data = file_op.read_csv("test.csv")
        self.assertIsNone(data)

    @patch('builtins.print')
    def test_save_to_csv_exception(self, mock_print):
        file_op = FileOperation()
        data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        with patch('pandas.DataFrame.to_csv') as mock_to_csv:
            mock_to_csv.side_effect = Exception("Test exception")
            file_op.save_to_csv(data, "test.csv")
        mock_print.assert_called_once_with("An error occurred while saving data to CSV file: Test exception")

    @patch('pandas.DataFrame.to_csv')
    def test_save_to_csv_success(self, mock_to_csv):
        file_op = FileOperation()
        data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        file_op.save_to_csv(data, "test.csv")
        mock_to_csv.assert_called_once_with("test.csv", index=False)


if __name__ == '__main__':
    unittest.main()