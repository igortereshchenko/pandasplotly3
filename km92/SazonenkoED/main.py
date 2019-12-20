# import os
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keys.json"

from bq_helper import BigQueryHelper

bq_assistant = BigQueryHelper('bigquery_public_data', 'nhtsa-traffic-fatalities')

