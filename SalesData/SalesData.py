import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



class SalesData:
    def __init__(self, data):
        self.data = data
#4
    def eliminate_duplicates(self):
        """
        Eliminate duplicate rows in the dataset to ensure data integrity and consistency.
        """
        if self.data is not None:
            self.data = self.data.drop_duplicates().dropna()
#5
    def calculate_total_sales(self):
        """
        Calculate the total sales for each product.

        Returns:
        DataFrame: DataFrame with total sales for each product.
        """
        self.data['Total Sales'] = self.data['Quantity'] * self.data['Price']

#6
    def _calculate_total_sales_per_month(self):
        """
        Calculate the total sales for each month.

        Returns:
        DataFrame: DataFrame with total sales for each month.
        """
        if 'Total Sales' not in self.data.columns:
            self.calculate_total_sales()
        self.data['Date'] = pd.to_datetime(self.data['Date'], dayfirst=True, errors='coerce')
        self.data['Month'] = self.data['Date'].dt.month
        total_sales_per_month= self.data.groupby('Month')['Total Sales'].sum()

        return total_sales_per_month
#7
    def _identify_best_selling_product(self):
        """
        Identify the best-selling product.

        Returns:
        str: Best-selling product.
        """
        if 'Total Sales' not in self.data.columns:
            self.calculate_total_sales()
        best_selling_product = self.data.groupby('Product')['Total Sales'].sum().idxmax()
        return best_selling_product
#8
    def _identify_month_with_highest_sales(self):
        """
        Identify the month with the highest total sales.

        Returns:
        int: Month with the highest total sales.
        """
        monthly_sales = self._calculate_total_sales_per_month()
        month_with_highest_sales = monthly_sales.idxmax()
        return month_with_highest_sales
#9
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
#10
    def add_to_dict(self, analysis_results):
        # Calculate additional values
        if 'Total Sales' not in self.data.columns:
            self.calculate_total_sales()
        minimest_selling_product = self.data.groupby('Product')['Total Sales'].sum().idxmin()
        average_sales = self.data['Total Sales'].mean()

        analysis_results['minimest_selling_product'] = minimest_selling_product
        analysis_results['average_sales'] = average_sales

        return  analysis_results
#11
    def calculate_cumulative_sales(self):
        """
        Calculate the cumulative sum of sales for each product across months.

        Returns:
        DataFrame: DataFrame with cumulative sales for each product.
        """
        if 'Total Sales' not in self.data.columns:
            self.calculate_total_sales()
        if 'Month' not in self.data.columns:
            self.data['Date'] = pd.to_datetime(self.data['Date'], dayfirst=True, errors='coerce')
            self.data['Month'] = self.data['Date'].dt.month
        self.data['CumulativeSales'] = self.data.groupby(['Product', 'Month'])['Total Sales'].cumsum()
#12


    def add_90_percent_values_column(self):
        """
        Create a new column in the SalesData DataFrame that contains the 90% values of the 'Quantity' column.
        """
        if 'Quantity' in self.data.columns:
            quantile_90 = self.data['Quantity'].quantile(0.9)
            self.data['90%_Values'] = np.where(self.data['Quantity'] > quantile_90, 1, 0)
#13
    def bar_chart_category_sum(self):
        """
        Plot a bar chart to represent the sum of quantities sold for each product.
        """
        category_sum = self.data.groupby('Product')['Quantity'].sum()
        category_sum.plot(kind='bar', title='Sum of Quantities Sold for Each Product')
        plt.xlabel('Product')
        plt.ylabel('Sum of Quantities Sold')
        plt.show()

#14
    def calculate_mean_quantity(self):
        """
        Calculate the mean, median, and second max for Total column using NumPy array manipulation.

        Returns:
        tuple: Tuple containing mean, median, and second max values.
        """
        mean = np.mean(self.data['Total'])
        median = np.median(self.data['Total'])
        sorted_totals = np.sort(self.data['Total'])
        second_max = sorted_totals[-2]
        return mean, median, second_max
#15

    def filter_by_sellings_or(self):
        condition = (self.data['Quantity'] > 5) | (self.data['Quantity'] == 0)
        filtered_data = self.data[condition]
        return filtered_data
# 15
    def filter_by_sellings_and(self):
        condition = (self.data['Price'] > 300) & (self.data['Quantity'] < 2)
        filtered_data = self.data[condition]
        return filtered_data
#16
    def divide_by_2(self):
        """
        Divide all values in the SalesData DataFrame by 2 for "BLACK FRIDAY". Column name will be "BlackFridayPrice".
        """
        self.data['BlackFridayPrice'] = self.data['Price'].div(2)
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
            if col in self.data.columns:
                col_data = self.data[col]
                if col_data.dtype.kind in 'biufc':
                    col_stats = {
                        'max': col_data.max(),
                        'sum': col_data.sum(),
                        'abs': col_data.abs().sum(),
                        'cumulative_max': col_data.cummax()
                    }
                    stats[col] = col_stats

        return stats
