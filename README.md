# NYC Taxi Data Pipeline 🚕

## 📌 Project Overview
This project is an **ETL pipeline** that extracts New York City taxi trip data from a public **parquet file**, loads it into a **PostgreSQL database** running in a Docker container, and enables querying via **pgAdmin**.

## ⚙️ Tech Stack
- **Python** (Data ingestion and transformation)
- **Docker & Docker-Compose** (Containerized database setup)
- **PostgreSQL** (Relational database for storing taxi trip data)
- **pgAdmin** (GUI for managing the database)
- **Pandas & SQL** (Data processing and querying)

## 🚀 Features
- **Extract**: Fetches a parquet file from an external source.
- **Transform**: Parses and prepares the data for database ingestion.
- **Load**: Loads data into a PostgreSQL database running in a Docker container.
- **Query**: Access and analyze data via **pgAdmin**.

## 📂 Project Structure
```
📁 ny-taxi-data-pipeline/
│── docker-compose.yml  # Compose file for PostgreSQL & pgAdmin
│── ingest_data.py      # Fetches parquet file & loads into PostgreSQL
│── .gitignore               # Ignores large and sensitive files
│── README.md                # Project documentation
```

## 🛠️ Setup & Usage

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/fensals/ny-taxi-data-pipeline.git
cd ny-taxi-data-pipeline
```

### **2️⃣ Start Docker Services**
Ensure **Docker** is installed and running, then start the PostgreSQL & pgAdmin containers:
```sh
docker-compose up -d
```

### **3️⃣ Run the Python Ingestion Script**
```sh
python scripts/ingest_data.py
```

### **4️⃣ Access the Database in pgAdmin**
- Open **pgAdmin** in your browser: [http://localhost:5050](http://localhost:5050)
- Use the credentials from **`docker-compose.yml`**.

## 📊 Example SQL Query
```sql
SELECT passenger_count, COUNT(*) AS num_trips
FROM yellow_taxi_data
GROUP BY passenger_count
ORDER BY num_trips DESC;
```

## 📖 Resources
- NYC Taxi Dataset: [Google Cloud Public Datasets](https://console.cloud.google.com/marketplace/details/nyc-tlc/nyc-tlc-trips)
- Docker Documentation: [https://docs.docker.com/](https://docs.docker.com/)
- PostgreSQL: [https://www.postgresql.org/](https://www.postgresql.org/)

## 🤝 Contributing
Feel free to open an issue or submit a pull request if you have ideas or improvements.

## 📜 License
This project is open-source and available under the **MIT License**.
