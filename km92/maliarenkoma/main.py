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

plot(dict(data=[bar], layout=bar_layout))

by_vehicles = [
    df[df['vehicle_number'] == 5],
    df[df['vehicle_number'] == 1],
    df[df['vehicle_number'] == 9],
]

scatter_data = [el.groupby(["state_number"])["state_number"].count() for el in by_vehicles]

sc_1 = go.Scatter(
    x=scatter_data[0].index,
    y=scatter_data[0].values,
    name="vehicle id 5"
)

sc_2 = go.Scatter(
    x=scatter_data[1].index,
    y=scatter_data[1].values,
    name="vehicle id 1"
)

sc_3 = go.Scatter(
    x=scatter_data[2].index,
    y=scatter_data[2].values,
    name="vehicle id 9"
)

scatter_layout = dict(
    title='Num Accidents by vehicle_id in state',
    xaxis=dict(title='state', ),
    yaxis=dict(title='number'),
)

plot(dict(data=[sc_1, sc_2, sc_3], layout=scatter_layout))
