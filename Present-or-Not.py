import pandas as pd

# Sample data
data = {'col1': [1, 2, 3, 4, 7],
        'col2': [4, 5, 6, 9, 5],
        'col3': [7, 8, 12, 1, 11]}

df = pd.DataFrame(data)

# Check if the columns are present
columns_to_check = ['Col4', 'col1']

for col in columns_to_check:
    if col in df.columns:
        print(f"{col} is present in DataFrame.")
    else:
        print(f"{col} is not present in DataFrame.")
