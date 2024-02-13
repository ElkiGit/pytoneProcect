import numpy as np
import pandas as pd
import seaborn as sns

from SalesData import SalesData

if __name__ == '__main__':

    # Create SalesData instance with sample data
    data = pd.DataFrame({
        'Product': ['A', 'B', 'A', 'C', 'B'],
        'Sales': [100, 200, 150, 300, 250],
        'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05']
    })

    sales_data = SalesData(data)

    # Perform operations
    sales_data.eliminate_duplicates()
    total_sales = sales_data.calculate_total_sales()
    cumulative_sales = sales_data.calculate_cumulative_sales()

    # Display results
    print("Total Sales:")
    print(total_sales)
    print("\nCumulative Sales:")
    print(cumulative_sales)

    # Plot a bar chart
    sales_data.bar_chart_category_sum()
