import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Load values from .env file
load_dotenv()

host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
database = os.getenv("DB_NAME")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")

# Create PostgreSQL connection
engine = create_engine(
    f"postgresql+psycopg://{user}:{password}@{host}:{port}/{database}"
)

processed_folder = "data/processed"

# Read each processed CSV file
for file in os.listdir(processed_folder):

    if file.endswith(".csv"):

        file_path = os.path.join(processed_folder, file)

        df = pd.read_csv(file_path)

        # Create a clean PostgreSQL table name
        table_name = file.replace(".csv", "")
        table_name = table_name.replace("_dataset", "")
        table_name = table_name.replace("olist_", "")

        print(f"Loading {file} -> {table_name}")

        # Load dataframe into PostgreSQL
        df.to_sql(
            table_name,
            engine,
            if_exists="replace",
            index=False
        )

        print(f"Loaded {len(df)} rows")

print("\nAll tables loaded successfully!")