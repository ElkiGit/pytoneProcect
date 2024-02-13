import pandas as pd
from FileOperation import FileOperation

if __name__ == '__main__':
    file_op = FileOperation()

    # Read data from a CSV file
    data = file_op.read_csv("../YafeNof.csv")
    if data is not None:
        print("Data read from CSV file:")
        print(data)

    # Save data to a new CSV file
    new_data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    file_op.save_to_csv(new_data, "out.csv")