FROM python:3.10

RUN pip install pandas requests sqlalchemy psycopg2 pyarrow

WORKDIR /app

COPY ingest_data.py ingest_data.py

ENTRYPOINT ["python", "ingest_data.py"]

