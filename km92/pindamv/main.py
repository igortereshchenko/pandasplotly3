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
        LIMIT 100
        """

df = bq_assistant.query_to_pandas(QUERY)
print(df)

x = df.state_number

bar = go.Bar(
    x= x,
    y = df.non_motorist_action_circumstances,
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


