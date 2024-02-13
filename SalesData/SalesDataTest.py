import unittest
import pandas as pd
from unittest.mock import patch
import numpy as np
import seaborn as sns

from SalesData import SalesData


class TestSalesData(unittest.TestCase):
    def setUp(self):
        self.data = pd.DataFrame({
            'Product': ['A', 'B', 'A', 'C', 'B'],
            'Sales': [100, 200, 150, 300, 250],
            'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05']
        })
        self.sales_data = SalesData(self.data)

    # def test_eliminate_duplicates(self):
    #     self.sales_data.eliminate_duplicates()
    #     self.assertEqual(len(self.sales_data.Product), 4)

    def test_calculate_total_sales(self):
        total_sales = self.sales_data.calculate_total_sales()
        self.assertEqual(len(total_sales), 3)

    def test_calculate_cumulative_sales(self):
        self.sales_data.calculate_cumulative_sales()
        self.assertIn('CumulativeSales', self.sales_data.data.columns)

    def test_bar_chart_category_sum(self):
        with patch('seaborn.barplot') as mock_barplot:
            self.sales_data.bar_chart_category_sum()
            mock_barplot.assert_called_once()
    #
    # def test_filter_by_sellings_or_and(self):
    #     filtered_data = self.sales_data.filter_by_sellings_or_and()
    #     self.assertEqual(len(filtered_data), 2)

    # def test_divide_by_2(self):
    #     self.sales_data.divide_by_2()
    #     self.assertIn('BlackFridayPrice', self.sales_data.data.columns)

    def test_calculate_stats(self):
        stats = self.sales_data.calculate_stats()
        self.assertEqual(len(stats), 3)
        self.assertIsInstance(stats['Sales']['maximum'], np.int64)
        self.assertIsInstance(stats['Sales']['sum'], np.int64)
        self.assertIsInstance(stats['Sales']['absolute_values'], np.int64)
        self.assertIsInstance(stats['Sales']['cumulative_maximum'], np.int64)


if __name__ == '__main__':
    unittest.main()
