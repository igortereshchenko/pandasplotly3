import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keys.json"

import pandas as pd
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot

bq_assistant = BigQueryHelper('bigquery-public-data', 'nhtsa-traffic-fatalities')

QUERY = """
        SELECT state_name,city,hour_of_crash,month_of_crash FROM `bigquery-public-data.nhtsa_traffic_fatalities.accident_2015`
        LIMIT 1000
        """

df = bq_assistant.query_to_pandas(QUERY)

b = df.groupby(["state_name"])['state_name'].count()


print(b)

print(type(b))

trace1 = go.Bar(
    x = b.index
    ,y = b.values
)

plot(trace1)
