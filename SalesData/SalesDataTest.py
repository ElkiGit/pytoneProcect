import unittest
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from SalesData import SalesData

# Import the SalesData class

from SalesData import SalesData
class TestSalesData(unittest.TestCase):
    def setUp(self):

        data = {
            'Customer ID': [1, 2, 3, 4, 5],
            'Date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05'],
            'Product': ['A', 'B', 'C', 'D', 'E'],
            'Price': [10, 20, 30, 40, 50],
            'Quantity': [2, 4, 6, 8, 10],
            'Total': [20, 80, 180, 320, 500]
        }
        self.sales_data = SalesData(pd.DataFrame(data))

    def test_eliminate_duplicates(self):
        # בדיקת הסרת רשומות כפולות
        self.sales_data.eliminate_duplicates()
        self.assertEqual(len(self.sales_data.data), len(self.sales_data.data.drop_duplicates()))

    def test_calculate_total_sales(self):
        # בדיקת חישוב סכום המכירות
        self.sales_data.calculate_total_sales()
        self.assertIn('Total Sales', self.sales_data.data.columns)

    def test_calculate_total_sales_per_month(self):
        # בדיקת חישוב סכום המכירות לפי חודש
        result = self.sales_data._calculate_total_sales_per_month()
        self.assertIsInstance(result, pd.Series)

    def test_identify_best_selling_product(self):
        """
        Test the _identify_best_selling_product method.
        """
        best_selling_product = self.sales_data._identify_best_selling_product()
        self.assertEqual(best_selling_product, 'E')

    def test_identify_month_with_highest_sales(self):
        """
        Test the _identify_month_with_highest_sales method.
        """
        month_with_highest_sales = self.sales_data._identify_month_with_highest_sales()
        self.assertEqual(month_with_highest_sales, 5)  # Assuming January is represented as 1

    def test_analyze_sales_data(self):
        """
        Test the analyze_sales_data method.
        """
        analysis_results = self.sales_data.analyze_sales_data()
        self.assertEqual(analysis_results['best_selling_product'], 'E')
        self.assertEqual(analysis_results['month_with_highest_sales'], 5)  # Assuming January is represented as 1

    def test_add_to_dict(self):
        """
        Test the add_to_dict method.
        """
        analysis_results = {'Total Sales': 1500}  # Assuming some initial results
        updated_results = self.sales_data.add_to_dict(analysis_results)
        self.assertEqual(updated_results['minimest_selling_product'], 'A')
        self.assertEqual(updated_results['average_sales'], 220)

    def test_calculate_cumulative_sales(self):
        """
        Test the calculate_cumulative_sales method.
        """
        cumulative_sales = self.sales_data.calculate_cumulative_sales()
        # You may add more assertions based on the expected output

    def test_add_90_percent_values_column(self):
        """
        Test the add_90_percent_values_column method.
        """
        self.sales_data.add_90_percent_values_column()
        self.assertIn('90%_Values', self.sales_data.data.columns)
        # You may add more assertions based on the expected output

    def test_calculate_cumulative_sales(self):
        """
        Test the calculate_cumulative_sales method.
        """
        cumulative_sales_df = self.sales_data.calculate_cumulative_sales()
        # Assuming some specific assertions about the cumulative sales DataFrame

    def test_add_90_percent_values_column(self):
        """
        Test the add_90_percent_values_column method.
        """
        self.sales_data.add_90_percent_values_column()
        self.assertIn('90%_Values', self.sales_data.data.columns)
        # Assuming some specific assertions about the '90%_Values' column

   # def test_bar_chart_category_sum(self):
        """
        Test the bar_chart_category_sum method.
        """
        # Capture standard output and error.
        #with captured_output() as (out, err):
            #self.sales_data.bar_chart_category_sum()

        # Check if the plot is generated
        #self.assertNotEqual(len(out.getvalue()), 0)

    def test_calculate_mean_quantity(self):
        """
        Test the calculate_mean_quantity method.
        """
        mean, median, second_max = self.sales_data.calculate_mean_quantity()
        # Assuming specific assertions about the calculated values

    def test_filter_by_sellings_or(self):
        """
        Test the filter_by_sellings_or method.
        """
        filtered_data = self.sales_data.filter_by_sellings_or()
        # Assuming specific assertions about the filtered data

    def test_filter_by_sellings_and(self):
        """
        Test the filter_by_sellings_and method.
        """
        filtered_data = self.sales_data.filter_by_sellings_and()
        # Assuming specific assertions about the filtered data

    def test_divide_by_2(self):
        """
        Test the divide_by_2 method.
        """
        self.sales_data.divide_by_2()
        self.assertIn('BlackFridayPrice', self.sales_data.data.columns)
        # Assuming some specific assertions about the new column

    def test_calculate_stats(self):
        """
        Test the calculate_stats method.
        """
        stats = self.sales_data.calculate_stats()
        # Assuming specific assertions about the calculated stats


if __name__ == '__main__':
    unittest.main()