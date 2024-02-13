import numpy as np
import pandas as pd
from FileOperation import FileOperation
from  SalesData import SalesData
import sys
#1

#E:\סוף הקורס\חומרים לפרויקט\YafeNof.csv
#C:\Users\שרי הימלפרב\Desktop\פרויקט גמר בפייתון\חומרים לפרויקט\YafeNof.csv


file_operation = FileOperation()

# Reading data from an Excel file
data = file_operation.read_excel("YafeNof.csv")
#print(data);

# Saving data to a new Excel file
#data_to_save = pd.DataFrame({'Column1': [1, 2, 3], 'Column2': ['S', 'B', 'C']})
#file_operation.save_to_excel(data_to_save, "output_file.xlsx")

#2

sales_data = SalesData(data)
sales_data.eliminate_duplicates()
sales_data.calculate_total_sales()
sales_data._calculate_total_sales_per_month()
sales_data._identify_best_selling_product()
sales_data._identify_month_with_highest_sales()
sales_data.analyze_sales_data()
sales_data.add_additional_values()

#3

sales_data.calculate_cumulative_sales()
sales_data.bar_chart_category_sum()
sales_data.calculate_mean_quantity()
sales_data.calculate_mean_quantity()
print(sales_data.calculate_stats())
sales_data.divide_by_2()
sales_data.categorize_prices()
print(sales_data.complex_data_transformation())
print(sales_data.data)



def print_python_version():
    print(sys.version)
print_python_version()

