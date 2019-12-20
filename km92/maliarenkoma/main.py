import os
import pandas as pd
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "keys.json"
LIMIT = 100

bq_assistant = BigQueryHelper('bigquery-public-data', 'nhtsa_traffic_fatalities')
QUERY = """
        SELECT state_number, vehicle_number, driver_maneuvered_to_avoid, driver_maneuvered_to_avoid_name   
        FROM `bigquery-public-data.nhtsa_traffic_fatalities.maneuver_2016`
        LIMIT {}
        """.format(LIMIT)

df: pd.DataFrame = bq_assistant.query_to_pandas(QUERY)

group_by_state = df.groupby(["state_number"])

bar_data = group_by_state["state_number"].count()
bar = go.Bar(
    x=bar_data.index,
    y=bar_data.values,
)
bar_layout = dict(
    title='Accidents',
    xaxis=dict(title='state', ),
    yaxis=dict(title='number'),
)

fig = dict(data=[bar], layout=bar_layout)
plot(fig)
