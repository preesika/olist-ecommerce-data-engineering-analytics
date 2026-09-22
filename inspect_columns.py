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

        for column in df.columns:
            print(column)