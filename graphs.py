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