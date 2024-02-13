import numpy as np
#import pandas as pd
import seaborn as sns

from FileOperation.FileOperation import FileOperation
from SalesData import SalesData

if __name__ == '__main__':
    file_op = FileOperation()
    # Create SalesData instance with sample data

    data = file_op.read_csv("../YafeNof.csv")
    sales_data = SalesData(data)

#4
    sales_data.eliminate_duplicates()
#5
    sales_data.calculate_total_sales()
#6
    total_sales_per_month = sales_data._calculate_total_sales_per_month()
#7
    best_selling_product=sales_data._identify_best_selling_product()
#8
    month_with_highest_sales=sales_data._identify_month_with_highest_sales()
#9
    analysis_results = sales_data.analyze_sales_data()
#10
    analysis_results=sales_data.add_to_dict(analysis_results)
#11
    sales_data.calculate_cumulative_sales()
#12
    sales_data.add_90_percent_values_column()
#13
    sales_data.bar_chart_category_sum()
#14
    results = sales_data.calculate_mean_quantity()
    print("Mean:", results[0])
    print("Median:", results[1])
    print("Second max:", results[2])
#15
    sales_data.filter_by_sellings_and()
    sales_data.filter_by_sellings_or()
#16
    sales_data.divide_by_2()
#17
    print(sales_data.calculate_stats())
