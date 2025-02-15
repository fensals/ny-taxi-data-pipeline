import pyarrow.parquet as pq
import pandas as pd
import requests
from sqlalchemy import create_engine

def download_parquet(url, output_path):
    """Downloads the Parquet file from the given URL to the specified local path."""
    print(f"📥 Downloading {url} ...")
    response = requests.get(url, stream=True)

    if response.status_code == 200:
        with open(output_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"✅ Download complete: {output_path}")
    else:
        raise Exception(f"Failed to download file: HTTP {response.status_code}")

def main(params):
    user = params['user']
    password = params['password']
    host = params['host']
    port = params['port']
    db = params['db']
    table_name = params['table_name']
    url = params['url']
    output_file = "yellow_tripdata.parquet"

    # Step 1: Download the Parquet file
    download_parquet(url, output_file)

    # Step 2: Read the Parquet file from the local system
    print("📖 Reading downloaded Parquet file...")
    table = pq.read_table(output_file)
    df = table.to_pandas()

    # Step 3: Connect to PostgreSQL
    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}")

    # Step 4: Create table schema (only headers first)
    df.head(0).to_sql(name=table_name, con=engine, if_exists='replace', index=False)

    # Step 5: Insert data in chunks
    chunk_size = 100000
    for start in range(0, len(df), chunk_size):
        df_chunk = df.iloc[start:start + chunk_size]
        df_chunk.to_sql(name=table_name, con=engine, if_exists='append', index=False)
        print(f"✅ Inserted rows {start} to {start + len(df_chunk)}")

    print("🎉 Data upload complete!")

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--user", required=True)
    parser.add_argument("--password", required=True)
    parser.add_argument("--host", required=True)
    parser.add_argument("--port", required=True)
    parser.add_argument("--db", required=True)
    parser.add_argument("--table_name", required=True)
    parser.add_argument("--url", required=True)

    args = parser.parse_args()
    main(vars(args))
