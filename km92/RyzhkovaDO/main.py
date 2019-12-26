import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "keys.json"
import numpy as np
import pandas as pd
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot


bg_assistant = BigQueryHelper('bigquery-public-data', 'nhtsa_traffic_fatalities')


QUERY = """
         SELECT * FROM  `bigquery-public-data.nhtsa_traffic_fatalities.maneuver_2016`
        LIMIT 1000
        """


df = bg_assistant.query_to_pandas(QUERY)


trace1 = go.Scatter(
                    x = df['state_number'],
                    y = df['vehicle_number'],
                    mode="lines",
                    )

fig_1 = dict(data=[trace1])
plot(fig_1)

trace2 = go.Bar(
    x = df["state_number"],
    y = df["driver_maneuvered_to_avoid_name"],
              )

fig_2 = go.Figure(data=[trace2])
plot(fig_2)


trace3 = go.Figure(data=[go.Pie(labels=df["driver_maneuvered_to_avoid_name"], values=df["vehicle_number"])])

plot(trace3)
