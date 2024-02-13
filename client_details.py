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
