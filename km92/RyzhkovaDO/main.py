import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "keys.json"
import numpy as np
import pandas as pd
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot
bg_assistant = BigQueryHelper('bigquery-public-data', 'nhtsa_traffic_fatalities')
QUERY = """
         SELECT * FROM `bigquery-public-data.nhtsa_traffic_fatalities.maneuver2016`
         LIMIT 10
        """
df = bg_assistant.query_to_pandas(QUERY)
trace1 = go.Scatter(
                    x = df['state_number - назва штату'],
                    y = df['vehicle_number'],
                    mode = "lines",
                    )

fig=dict(data=[trace1])
plot(fig)

trace2= go.Bar(
    x=["vehicle_number"],
    y=["driver_maneuvered_to_avoid_name"],
            )
fig=go.Figure(data=[trace2])
plot(fig)

trace3=go.Figure(data=[go.Pie(labels= "driver_maneuvered_to_avoid_name", values="vehicle_number")])

plot(trace3)

