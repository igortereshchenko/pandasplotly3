import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "keys.json"

import pandas as pd
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot

bq_assistant = BigQueryHelper('bigquery-public-data', 'nhtsa_traffic_fatalities')

QUERY = """
        SELECT consecutive_number, state_number, vehicle_number, condition_impairment_at_time_of_crash_driver
        FROM `bigquery-public-data.nhtsa_traffic_fatalities.drimpair_2016`
        LIMIT 10000
        """

df = bq_assistant.query_to_pandas(QUERY)

trace3 = go.Bar(
    x = df['state_number'].values,
    y = df['condition_impairment_at_time_of_crash_driver'].values


)

layout = go.Layout(
                   title=' distraction in states',
                   xaxis=dict(title='state'),
                   yaxis=dict( title='distraction type'),)

fig = dict(data = [trace3], layout = layout)

plot(fig)