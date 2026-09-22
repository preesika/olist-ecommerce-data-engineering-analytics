import pandas as pd
import os

data_folder = "data"

for file in os.listdir(data_folder):
    if file.endswith(".csv"):

        df = pd.read_csv(os.path.join(data_folder, file))

        missing = df.isnull().sum()
        missing = missing[missing > 0]

        if len(missing) > 0:
            print("\n================================")
            print(file)
            print("================================")

            for column, count in missing.items():
                percentage = (count / len(df)) * 100
                print(f"{column}: {count} ({percentage:.2f}%)")