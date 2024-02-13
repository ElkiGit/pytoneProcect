import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns




class SalesData:

    def __init__(self, data):
        self.data = data
#4

    def eliminate_duplicates(self):
        """
        Detects and eliminates duplicate rows in the dataset to ensure data integrity and consistency.
        """
        self.data = self.data.drop_duplicates().dropna()

#5

    def calculate_total_sales(self):
        """
        Calculates the total sales for each product.
        """
        self.data['Total Sales'] = self.data['Quantity'] * self.data['Price']

        # Create a pie chart using matplotlib
        total_sales_per_product = self.data.groupby('Product')['Total Sales'].sum()
        plt.figure(figsize=(8, 8))
        plt.pie(total_sales_per_product, labels=total_sales_per_product.index, autopct='%1.1f%%')
        plt.title('Total Sales for Each Product')
        plt.show()

        # Create a bar plot using seaborn
        sns.boxplot(x=total_sales_per_product.index, y=total_sales_per_product.values)
        plt.title('Total Sales for Each Product')
        plt.xlabel('Product')
        plt.ylabel('Total Sales')
        plt.show()

    #6
    def _calculate_total_sales_per_month(self):
        self.data['Date'] = pd.to_datetime(self.data['Date'], dayfirst=True, errors='coerce')
        self.data['Month'] = self.data['Date'].dt.month

        # Calculate total sales per month
        monthly_sales = self.data.groupby('Month')['Total Sales'].sum()

        # Plotting using matplotlib
        plt.figure(figsize=(10, 6))
        plt.plot(monthly_sales.index, monthly_sales.values, marker='o', color='blue', linestyle='-')
        plt.title('Total Sales per Month (Matplotlib)')
        plt.xlabel('Month')
        plt.ylabel('Total Sales')
        plt.xticks(range(1, 13))  # Assuming months are represented by integers from 1 to 12
        plt.grid(True)

        # Annotate each point with the total sales value
        for i, sales in enumerate(monthly_sales):
            plt.annotate(f'{sales}', (monthly_sales.index[i], monthly_sales.values[i]), textcoords="offset points",
                         xytext=(0, 10), ha='center')

        plt.show()

        # Plotting using seaborn
        sns.catplot(
            data=monthly_sales.reset_index(name='Total Sales'),
            kind="violin",
            x="Month", y="Total Sales"
        )
        plt.title('Total Sales per Month (Seaborn)')
        plt.xlabel('Month')
        plt.ylabel('Total Sales')
        plt.grid(True)
        plt.show()
        return monthly_sales

    #7
    def _identify_best_selling_product(self):
        """
        Identifies the best-selling product.
        """
        # Calculate total sales for each product
        product_sales = self.data.groupby('Product')['Total Sales'].sum()

        # Identify the best-selling product
        best_selling_product = product_sales.idxmax()

        # Plotting
        plt.figure(figsize=(8, 6))
        plt.bar(best_selling_product, product_sales.max(), color='skyblue')
        plt.title('Best-Selling Product')
        plt.xlabel('Product')
        plt.ylabel('Total Sales')
        plt.xticks(rotation=45)
        plt.show()

#8
    def _identify_month_with_highest_sales(self):
        """
        Identifies the month with the highest total sales.
        """
        # Calculate total sales for each month
        monthly_sales = self._calculate_total_sales_per_month()

        # Identify the month with the highest total sales
        month_with_highest_sales = monthly_sales.idxmax()

        # Plotting
        plt.figure(figsize=(8, 6))
        plt.bar(monthly_sales.index, monthly_sales.values, color='skyblue')
        plt.scatter(month_with_highest_sales, monthly_sales.max(), color='red', marker='o', s=100,
                    label='Highest Sales Month')
        plt.title('Highest Sales Month')
        plt.xlabel('Month')
        plt.ylabel('Total Sales')
        plt.xticks(monthly_sales.index)
        plt.legend()
        plt.grid(True)
        plt.show()

#9
    def analyze_sales_data(self):
        """
        Performs analysis using the previously defined private methods and returns a dictionary.

        Returns:
        - dict: Analysis results with keys 'best_selling_product' and 'month_with_highest_sales'.
        """
        self.eliminate_duplicates()
        self.calculate_total_sales()

        best_selling_product = self._identify_best_selling_product()
        month_with_highest_sales = self._identify_month_with_highest_sales()

        analysis_results = {
            'best_selling_product': best_selling_product,
            'month_with_highest_sales': month_with_highest_sales
        }
        return analysis_results

#10
    def add_additional_values(self):
        """
        Adds additional values to the analysis dictionary:
        - 'minimest_selling_product': the product with the minimum total sales.
        - 'average_sales': the average of the sales for all months.
        """
        self.calculate_total_sales()

        minimest_selling_product = self.data.groupby('Product')['Total Sales'].sum().idxmin()
        average_sales = self.data['Total Sales'].mean()

        analysis_results = self.analyze_sales_data()
        analysis_results['minimest_selling_product'] = minimest_selling_product
        analysis_results['average_sales'] = average_sales

        return analysis_results

    #11
    def calculate_cumulative_sales(self):
        """
        Calculate the cumulative sum of sales for each product across months.
        """
        # Calculate cumulative sales
        self.data['Cumulative Sales'] = self.data.groupby(['Product', 'Month'])['Total Sales'].cumsum()

        # Plotting
        plt.figure(figsize=(10, 6))
        for product, group in self.data.groupby('Product'):
            plt.plot(group['Month'], group['Cumulative Sales'], label=product)
        plt.title('Cumulative Sales for Each Product Across Months')
        plt.xlabel('Month')
        plt.ylabel('Cumulative Sales')
        plt.legend()
        plt.grid(True)
        plt.show()


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
        Calculate the mean, median, and second max for the 'Total Sales' column.
        """
        mean_value = self.data['Total Sales'].mean()
        median_value = self.data['Total Sales'].median()
        second_max_value = self.data['Total Sales'].nlargest(2).iloc[-1]
        return mean_value, median_value, second_max_value



    #16
    def divide_by_2(self):
        # Divide prices by 2
        self.data['BlackFridayPrice'] = self.data['Price'].div(2)

        # Plot a comparison of original prices and Black Friday prices
        plt.figure(figsize=(8, 6))
        self.data[['Price', 'BlackFridayPrice']].plot(kind='bar')
        plt.title('Comparison of Original Prices and Black Friday Prices')
        plt.xlabel('Product')
        plt.ylabel('Price')
        plt.xticks(rotation=45)
        plt.legend(['Original Price', 'Black Friday Price'])
        plt.grid(True)
        plt.show()
    #17
    def calculate_stats(self, columns=None):
        if columns is None:
            columns = self.data.columns

        stats = {}

        for col in columns:
            if col in self.data.columns:
                col_data = self.data[col]
                if col_data.dtype.kind in 'biufc':  # Check if data type is numeric
                    col_stats = {
                        'max': col_data.max(),
                        'sum': col_data.sum(),
                        'abs': col_data.abs().sum(),
                        'cumulative_max': col_data.cummax()
                    }
                    stats[col] = col_stats

        return stats
    #19
    def categorize_prices(self):
        # Define bins and labels for categorizing prices
        bins = [0, 100, 200, 300, float('inf')]
        labels = ['Low', 'Medium', 'High', 'Very High']

        # Categorize prices
        self.data['Price_Category'] = pd.cut(self.data['Price'], bins=bins, labels=labels, right=False)

        # Plot the distribution of price categories
        plt.figure(figsize=(8, 6))
        self.data['Price_Category'].value_counts().plot(kind='bar', color='skyblue', edgecolor='black')
        plt.title('Distribution of Price Categories')
        plt.xlabel('Price Category')
        plt.ylabel('Frequency')
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.show()

        sns.catplot(data=self.data, x='Price_Category', kind='swarm', color='red')
        plt.title('Distribution of Price Categories')
        plt.xlabel('Price Category')
        plt.ylabel('Frequency')
        plt.xticks(rotation=45)
        plt.show()


    #22
    def complex_data_transformation(self):
        # Transpose the DataFrame
        transposed_df = self.data.transpose()

        return transposed_df



