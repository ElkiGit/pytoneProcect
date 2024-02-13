import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from FileOperation.FileOperation import FileOperation
from SalesData.SalesData import SalesData

# Press the green button in the gutter to run the script.
if __name__ == '__main__':


    # Create instances of the classes with sample data
    file_op = FileOperation()
    sales_data = SalesData(pd.DataFrame({
        'Product': ['A', 'B', 'C', 'A', 'B', 'C'],
        'Sales': [100, 200, 150, 300, 250, 200],
        'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05', '2023-01-06']
    }))

    # Matplotlib Plot Types
    # 1. Line Plot
    plt.plot(sales_data.data['Date'], sales_data.data['Sales'])
    plt.title('Line Plot')
    plt.xlabel('Date')
    plt.ylabel('Sales')
    plt.xticks(rotation=45)
    plt.show()

    # 2. Bar Plot
    plt.bar(sales_data.data['Product'], sales_data.data['Sales'])
    plt.title('Bar Plot')
    plt.xlabel('Product')
    plt.ylabel('Sales')
    plt.show()

    # 3. Horizontal Bar Plot
    plt.barh(sales_data.data['Product'], sales_data.data['Sales'])
    plt.title('Horizontal Bar Plot')
    plt.xlabel('Sales')
    plt.ylabel('Product')
    plt.show()

    # 4. Box Plot
    plt.boxplot(sales_data.data['Sales'])
    plt.title('Box Plot')
    plt.ylabel('Sales')
    plt.show()

    # 5. Violin Plot
    plt.violinplot(sales_data.data['Sales'])
    plt.title('Violin Plot')
    plt.ylabel('Sales')
    plt.show()

    # 6. Histogram
    plt.hist(sales_data.data['Sales'])
    plt.title('Histogram')
    plt.xlabel('Sales')
    plt.ylabel('Frequency')
    plt.show()

    # 7. Pie Chart
    plt.pie(sales_data.data['Sales'], labels=sales_data.data['Product'], autopct='%1.1f%%')
    plt.title('Pie Chart')
    plt.show()

    # Seaborn Plot Types
    # 1. Seaborn Line Plot
    sns.lineplot(x=sales_data.data['Date'], y=sales_data.data['Sales'])
    plt.title('Seaborn Line Plot')
    plt.xlabel('Date')
    plt.ylabel('Sales')
    plt.xticks(rotation=45)
    plt.show()

    # 2. Seaborn Bar Plot
    sns.barplot(x=sales_data.data['Product'], y=sales_data.data['Sales'])
    plt.title('Seaborn Bar Plot')
    plt.xlabel('Product')
    plt.ylabel('Sales')
    plt.show()

    # 3. Seaborn Box Plot
    sns.boxplot(sales_data.data['Sales'])
    plt.title('Seaborn Box Plot')
    plt.ylabel('Sales')
    plt.show()

    # 4. Seaborn Violin Plot
    sns.violinplot(sales_data.data['Sales'])
    plt.title('Seaborn Violin Plot')
    plt.ylabel('Sales')
    plt.show()

    # 5. Seaborn Histogram
    sns.histplot(sales_data.data['Sales'])
    plt.title('Seaborn Histogram')
    plt.xlabel('Sales')
    plt.ylabel('Frequency')
    plt.show()

#     # Example Usage:
#     # Create an instance of the FileOperation class
#
#     print("2222222222222222222222222222222222222")
#     # Example Usage:
#     # Create a SalesData object with sample data
#     data = {
#         'Date': ['2024-01-01', '2024-01-02', '2024-02-01', '2024-02-02'],
#         'Product': ['A', 'B', 'A', 'B'],
#         'Sales': [100, 200, 150, 250]
#     }
#
#     sales_data = SalesData(pd.DataFrame(data))
#
#     # Eliminate duplicates
#     sales_data.eliminate_duplicates()
#
#     # Analyze sales data
#     # data = None
#     analysis_results = sales_data.analyze_sales_data()
#     print("Analysis Results:")
#     print(analysis_results)
#     print(sales_data.add_to_dict(analysis_results))
#
#     data = {
#         'Product': ['A', 'B', 'A', 'B', 'A', 'B'],
#         'Sales': [100, 200, 150, 250, 300, 350],
#         'Quantity': [5, 10, 15, 20, 25, 30],
#         'Price': [200, 300, 400, 500, 600, 700],
#         'Selling': [7, 2, 6, 1, 0, 9],
#         'Total': [1000, 2000, 1500, 2500, 3000, 3500]
#     }
#     sales_data = SalesData(pd.DataFrame(data))
#
#     # Calculate cumulative sales
#     sales_data.calculate_cumulative_sales()
#
#     # Add 90% values column
#     sales_data.add_90_percent_values_column()
#
#     # Plot bar chart for category sum
#     sales_data.bar_chart_category_sum()
#
#     # Calculate mean quantity
#     mean_quantity_stats = sales_data.calculate_mean_quantity()
#     print("Mean Quantity Stats:", mean_quantity_stats)
#
#     # Filter by sellings or/and
#     filtered_data = sales_data.filter_by_sellings_or_and()
#
#     # Divide by 2 for Black Friday
#     sales_data.divide_by_2()
#
#     # Calculate stats for all columns
#     all_stats = sales_data.calculate_stats()
#     print("Stats for all columns:", all_stats)
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
#

import random
import sys
import datetime
import pandas as pd


# Decorator to handle errors and add timestamps
def handle_errors(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            print(f"<{datetime.datetime.now()}, {type(e).__name__}> {e} <{datetime.datetime.now()}>")
            result = None
        return result
    return wrapper


# Function to read additional files
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
        return data
    except FileNotFoundError as e:
        print(f"<{datetime.datetime.now()}, FileNotFoundError> {e} <{datetime.datetime.now()}>")
        return None


# Function to extract sales number and highest amount paid
def extract_info(product_name):
    # Example implementation, replace with actual logic
    sales_number = random.randint(1, 100)
    highest_amount_paid = random.randint(100, 1000)
    return sales_number, highest_amount_paid


# Function to execute unknown number of parameters
def execute_params(*args, **kwargs):
    result = {}
    for arg in args:
        if isinstance(arg, (int, float)):
            print(arg)
        elif isinstance(arg, tuple):
            key, value = arg
            result[key] = value
    return result


@handle_errors
def main():
    # Task 2: Reading additional files
    file_content = read_file("additional_file.txt")
    if file_content:
        print("File content:")
        print(file_content)

    # Task 3: Extracting sales number and highest amount paid for a product
    product_name = "Example Product"
    sales_number, highest_amount_paid = extract_info(product_name)
    print(f"Sales number for {product_name}: {sales_number}")
    print(f"Highest amount paid for {product_name}: {highest_amount_paid}")

    # Task 4: Printing Python version
    print("Python version:", sys.version)

    # Task 5: Execute a function with unknown number of parameters
    params_result = execute_params(10, 20, ("key1", "value1"), ("key2", "value2"), 30)
    print("Result of executing unknown parameters:", params_result)

    # Task 6: Print main table
    data = pd.DataFrame({'A': range(10), 'B': range(10, 20)})
    print("First 3 rows:")
    print(data.head(3))
    print("Last 2 rows:")
    print(data.tail(2))
    print("Random row:")
    print(data.sample())

    # Task 7: Iterate through numerical values in table
    for column in data.select_dtypes(include=['number']).columns:
        for value in data[column]:
            print(value)


if __name__ == "__main__":
    main()
