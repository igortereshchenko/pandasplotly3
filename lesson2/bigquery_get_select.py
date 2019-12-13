import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keys.json"

from google.cloud import bigquery


client = bigquery.Client()


QUERY = """
        SELECT * FROM `bigquery-public-data.new_york.citibike_trips`
        LIMIT 3
        """

query_job = client.query(QUERY)  # API request
rows = query_job

for row in rows:
    print(row)