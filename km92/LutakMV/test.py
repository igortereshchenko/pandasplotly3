import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keys.json"

import pandas as pd
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot

bq_assistant = BigQueryHelper('bigquery-public-data' , 'nhtsa_traffic_fatalities')


QUERY = """
        SELECT * FROM `bigquery-public-data.nhtsa_traffic_fatalities.drimpair_2016`
        LIMIT 1000
        """


df = bq_assistant.query_to_pandas(QUERY)
#print(df)




trace1 = go.Scatter(
            x = df.consecutive_number,
            y = df.condition_impairment_at_time_of_crash_driver,
            mode = 'markers',
            name = '',
            marker = dict(color = 'red'),
            text = df.vehicle_number
                    )
data = [trace1]

layout = dict(
              title = '',
              xaxis= dict(title= 'Номером регістру, присвоєний кожній аварії'),
              yaxis=dict(title='Порушення водія, які, можливо, сприяли аварії'),
             )
fig = dict(data = [trace1], layout = layout)
#plot(fig)


# trace2 = go.Pie(
#
#
#                     )
#
trace3 = go.Bar(
             x=df.state_number,
             y= df.consecutive_number,
             name = '',
             marker = dict(color = 'red',
                           line = dict(color = 'green',
                                       width = 1.2)),
             text = df.vehicle_number

              )
data1 = [trace3]
layout1 = dict(
              title = '',
              xaxis= dict(title= 'стан аварії'),
              yaxis=dict(title='номером регістру, присвоєний кожній аварії'),
             )
fig1 = dict(data = [trace3], layout = layout1)
plot(fig1)

