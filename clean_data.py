import pandas as pd
import os

raw_folder = "data/raw"
processed_folder = "data/processed"

os.makedirs(processed_folder, exist_ok=True)

for file in os.listdir(raw_folder):

    if file.endswith(".csv"):

        input_path = os.path.join(raw_folder, file)
        output_path = os.path.join(processed_folder, file)

        # Extract
        df = pd.read_csv(input_path)

        # Transform
        if file == "olist_products_dataset.csv":
            df["product_category_name"] = (
                df["product_category_name"].fillna("unknown")
            )

        # Load cleaned CSV into processed folder
        df.to_csv(output_path, index=False)

        print(f"Processed: {file}")

print("\nAll datasets processed successfully!")