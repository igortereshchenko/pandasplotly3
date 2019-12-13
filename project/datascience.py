import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keys.json"

import pandas as pd
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot

bq_assistant = BigQueryHelper('bigquery-public-data', 'new_york')


QUERY = """
        SELECT starttime, stoptime, start_station_name, end_station_name, usertype, gender, birth_year FROM `bigquery-public-data.new_york.citibike_trips`
        LIMIT 10000
        """


df = bq_assistant.query_to_pandas(QUERY)



df['trip_duration'] = df['stoptime'] - df['starttime']
df['trip_duration_minutes'] = df['trip_duration'].dt.total_seconds().div(60).astype(int)

df['start_date'] = df['starttime'].dt.normalize()


female_df = df[df['gender']=='female'];
female_df_groupby = female_df.groupby(['start_date'])['trip_duration_minutes'].sum()


trace1 = go.Scatter(
                    x = female_df_groupby.index,
                    y = female_df_groupby.values,
                    mode = "lines",
                    name = "female",
                    )


male_df = df[df['gender']=='male'];
male_df_groupby = male_df.groupby(['start_date'])['trip_duration_minutes'].sum()

trace2 = go.Scatter(
                    x = male_df_groupby.index,
                    y = male_df_groupby.values,
                    mode = "lines+markers",
                    name = "male"
                    )
data = [trace1, trace2]

layout = dict(title = 'Riding',
              xaxis= dict(title= 'days'),
              yaxis=dict(title='minutes'),
             )
fig = dict(data = [trace1, trace2], layout = layout)
plot(fig)

# most popular start point
start_point_groupby = df.groupby(['start_station_name'])['start_station_name'].count()

fig = {
  "data": [
    {
      "y": start_point_groupby.values,
      "x": start_point_groupby.index,
      "name": "Station name",
      "type": "bar"
    },
  ],
  "layout": {
        "title":"Station polularity",
    }
}
plot(fig)
