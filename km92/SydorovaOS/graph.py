import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "keys.json"

import pandas as pd
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot

bq_assistant = BigQueryHelper('bigquery-public-data', 'nhtsa_traffic_fatalities')

QUERY = """
        SELECT * FROM  `bigquery-public-data.nhtsa_traffic_fatalities.factor_2015`
        LIMIT 10000
        """

df = bq_assistant.query_to_pandas(QUERY)

print(df.state_number)
print(df.contributing_circumstances_motor_vehicle)

print()
trace1 = go.Scatter(
    x=df.state_number,
    y=df.contributing_circumstances_motor_vehicle,
    mode="markers",
    name="contributing_circumstances_motor_vehicle",
    marker=dict(color='blue'),
    text=df.vehicle_number
)

trace2 = go.Pie(


)

trace3 = go.Bar(
    x=df.state_number,
    y=df.contributing_circumstances_motor_vehicle,
    name="contributing_circumstances_motor_vehicle",
    marker=dict(color='blue', line=dict(color='red', width=1.5)),
    text=df.vehicle_number
)

data = [trace1]
data3 = [trace3]
data2 = [trace2]
layout = dict(
    title='',
    xaxis=dict(title=''),
    yaxis=dict(title=''),
)
fig = dict(data=[trace1], layout=layout)
fig3 = dict(data=[trace3], layout=layout)
fig2 = dict(data=[trace2], layout=layout)
plot(fig)
plot(fig3)
plot(fig2)
