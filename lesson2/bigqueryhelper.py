import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keys.json"

import pandas as pd
from bq_helper import BigQueryHelper


bq_assistant = BigQueryHelper('bigquery-public-data', 'new_york')

QUERY = """
        SELECT * FROM `bigquery-public-data.new_york.citibike_trips`
        """

print( bq_assistant.estimate_query_size(QUERY) ) #4.5 GB


QUERY = """
        SELECT * FROM `bigquery-public-data.new_york.citibike_trips`
        LIMIT 100
        """


df = bq_assistant.query_to_pandas(QUERY)

print(df.head(10))