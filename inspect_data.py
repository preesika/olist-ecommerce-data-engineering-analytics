import pandas as pd
import os

data_folder = "data"

for file in os.listdir(data_folder):
    if file.endswith(".csv"):
        file_path = os.path.join(data_folder, file)

        df = pd.read_csv(file_path)

        print("\n==============================")
        print(file)
        print("==============================")

        print("Rows:", len(df))
        print("Columns:", len(df.columns))
        print("Column names:")
        print(df.columns.tolist())