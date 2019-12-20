import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keys.json"

import pandas as pd
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot

bq_assistant = BigQueryHelper('bigquery-public-data', 'nhtsa_traffic_fatalities')

QUERY = """
        SELECT *
        FROM `bigquery-public-data.nhtsa_traffic_fatalities.nmprior_2015`
      
        """

df = bq_assistant.query_to_pandas(QUERY)
print(df)

x = df.vehicle_number

bar = go.Bar(
    x= x,
    y = df.sort_values(by = 'state_number', ascending=True),
    marker=dict(line=dict(color = 'green', width = 1.5)),
    name='Action circumstances'
)

layout = go.Layout(
    xaxis = {'title': 'State number'},
    barmode = 'group',
    title = 'Action circumstances statistics'
)
fig = go.Figure(data = [bar], layout = layout)
plot(fig)

x1 = df.sort_values(by = 'state_number', ascending=True)
scatter = go.Scatter(
    x = x1,
    y = df.non_motorist_action_circumstances,
    mode = 'lines'
)

layout2 = dict(
    title='Number of accidents in regions',
    xaxis = dict(title = 'Regions', zeroline = True),
    yaxis = dict(title = 'Number of accidents', zeroline = True)
)

fig2 = dict(data = [scatter], layout = layout2)
plot(fig2)

