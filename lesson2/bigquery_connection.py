import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keys.json"

import pandas as pd
from google.cloud import bigquery
from bq_helper import BigQueryHelper


client = bigquery.Client()


dataset_refference = client.dataset('new_york', project='bigquery-public-data')

print(type(dataset_refference))