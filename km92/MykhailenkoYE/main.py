import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keys.json"

import pandas as pd
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot

bq_assistant = BigQueryHelper('bigquery-public-data','nhtsa-traffic-fatalities')


QUERY = """
        SELECT damage_areas_name, vehicle_number, damaged_areas, consecutive_number FROM `bigquery-public-data.nhtsa_traffic_fatalities.damage_2015`
        LIMIT 10000
        """


df = bq_assistant.query_to_pandas(QUERY)


damaged_areas = df[df['traffic_crash'] == 'damaged_areas'];
damaged_areas_groupby = damaged_areas.groupby(["damaged_areas"])['damage_areas_name'].count()

trace1 = go.Scatter(
    x = damaged_areas_groupby.index,
    y = df.damaged_areas_groupby.values,
    mode = "lines",
    name = "crashes"

                    )
#
#
#
# trace2 = go.Pie(
#
#                     )
#
# trace3 = go.Bar(
#
# )
#
# data = [trace1]
#
# layout = dict(
#               title = '',
#               xaxis= dict(title= ''),
#               yaxis=dict(title=''),
#              )
fig = dict(data = [trace1])
plot(fig)

