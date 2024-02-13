import numpy as np
import pandas as pd
import seaborn as sns



class SalesData:
    def __init__(self, data):
        self.data = data

    def eliminate_duplicates(self):
        """
        Eliminate duplicate rows in the dataset to ensure data integrity and consistency.
        """
        if self.data is not None:
            self.data = self.data.drop_duplicates().dropna()

    def calculate_total_sales(self):
        """
        Calculate the total sales for each product.

        Returns:
        DataFrame: DataFrame with total sales for each product.
        """
        total_sales = self.data.groupby('Product')['Sales'].sum().reset_index()
        return total_sales

    def _calculate_total_sales_per_month(self):
        """
        Calculate the total sales for each month.

        Returns:
        DataFrame: DataFrame with total sales for each month.
        """
        self.data['Month'] = pd.to_datetime(self.data['Date']).dt.month
        total_sales_per_month = self.data.groupby('Month')['Sales'].sum().reset_index()
        return total_sales_per_month

    def _identify_best_selling_product(self):
        """
        Identify the best-selling product.

        Returns:
        str: Best-selling product.
        """
        best_selling_product = self.data.groupby('Product')['Sales'].sum().idxmax()
        return best_selling_product

    def _identify_month_with_highest_sales(self):
        """
        Identify the month with the highest total sales.

        Returns:
        int: Month with the highest total sales.
        """
        total_sales_per_month = self._calculate_total_sales_per_month()
        month_with_highest_sales = total_sales_per_month['Month'].iloc[total_sales_per_month['Sales'].idxmax()]
        return month_with_highest_sales

    def analyze_sales_data(self):
        """
        Perform the analysis using the previously defined private methods and return a dictionary.

        Returns:
        dict: Dictionary containing analysis results.
        """
        analysis_results = {}

        analysis_results['best_selling_product'] = self._identify_best_selling_product()
        analysis_results['month_with_highest_sales'] = self._identify_month_with_highest_sales()

        return analysis_results

    def add_to_dict(self, analysis_results):
        # Calculate additional values
        minimest_selling_product = self.data.groupby('Product')['Sales'].sum().idxmin()
        average_sales = self.data['Sales'].mean()

        analysis_results['minimest_selling_product'] = minimest_selling_product
        analysis_results['average_sales'] = average_sales

        return  analysis_results

    def calculate_cumulative_sales(self):
        """
        Calculate the cumulative sum of sales for each product across months.

        Returns:
        DataFrame: DataFrame with cumulative sales for each product.
        """
        cumulative_sales = self.data.groupby('Product')['Sales'].cumsum()
        self.data['CumulativeSales'] = cumulative_sales

    def add_90_percent_values_column(self):
        """
        Create a new column in the SalesData DataFrame that contains the 90% values of the 'Quantity' column.
        """
        if 'Quantity' in self.data.columns:
            quantile_90 = self.data['Quantity'].quantile(0.9)
            self.data['90%_Values'] = np.where(self.data['Quantity'] > quantile_90, 1, 0)

    def bar_chart_category_sum(self):
        """
        Plot a bar chart to represent the sum of quantities sold for each product.
        """
        sns.barplot(x='Product', y='Quantity', data=self.data, estimator=sum)

    def calculate_mean_quantity(self):
        """
        Calculate the mean, median, and second max for Total column using NumPy array manipulation.

        Returns:
        dict: Dictionary containing mean, median, and second max values.
        """
        mean = np.mean(self.data['Total'])
        median = np.median(self.data['Total'])
        sorted_totals = np.sort(self.data['Total'])
        second_max = sorted_totals[-2]
        return {'mean': mean, 'median': median, 'second_max': second_max}

    def filter_by_sellings_or_and(self):
        """
        Filter specific products by the following conditions:
        1. If number of selling more than 5 or number of selling == 0.
        2. If the price above 300 $ and sold less than 2 times.
        """
        filtered_data = self.data[(self.data['Selling'] > 5) | (self.data['Selling'] == 0) |
                                  ((self.data['Price'] > 300) & (self.data['Selling'] < 2))]
        return filtered_data

    def divide_by_2(self):
        """
        Divide all values in the SalesData DataFrame by 2 for "BLACK FRIDAY". Column name will be "BlackFridayPrice".
        """
        self.data['BlackFridayPrice'] = self.data['Price'] / 2

    def calculate_stats(self, columns=None):
        """
        Find the maximum, sum, absolute values, and cumulative maximum of the SalesData DataFrame for all
        columns, and for every column separately (depends on columns, if None: all).

        Parameters:
        columns (str or list): List of column names to calculate stats for. If None, stats will be calculated for all columns.

        Returns:
        dict: Dictionary containing stats for each column.
        """
        if columns is None:
            columns = self.data.columns

        stats = {}
        for col in columns:
            # Convert column to numeric type
            self.data[col] = pd.to_numeric(self.data[col], errors='coerce')
            col_data = self.data[col]
            stats[col] = {
                'maximum': col_data.max(),
                'sum': col_data.sum(),
                'absolute_values': col_data.apply(lambda x: pd.to_numeric(x, errors='coerce')).abs().sum(),
                'cumulative_maximum': col_data.cummax().max()
            }
        return stats
