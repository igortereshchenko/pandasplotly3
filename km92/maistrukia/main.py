import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keys.json"

import pandas as pd
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot

bq_assistant = BigQueryHelper('bigquery-public-data', 'nhtsa_traffic_fatalities')


QUERY = """
        SELECT state_number, state_name, number_of_motor_vehicles_in_transport_mvit, number_of_persons_in_motor_vehicles_in_transport_mvit FROM `bigquery-public-data.nhtsa_traffic_fatalities.accident_2015`
        LIMIT 10000
        """

df = pd.DataFrame(bq_assistant.query_to_pandas(QUERY))

state_group = df.groupby("state_name").count()

print(state_group)
#print(state_group.keys())

Bar_trace = go.Bar(
                    x = df["state_name"],
                    y = df["number_of_motor_vehicles_in_transport_mvit"],
                    name = "crash",
                    )

layout = dict(title = 'Crash',
              xaxis= dict(title= 'states'),
              yaxis=dict(title='cars'),
             )

fig = dict(data = [Bar_trace], layout = layout)
plot(fig)