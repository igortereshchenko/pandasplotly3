import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keys.json"

import pandas as pd
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot

bq_assistant = BigQueryHelper('bigquery-public-data','nhtsa_traffic_fatalities')


QUERY = """
        SELECT state_code, sequence_of_events_name, area_of_impact_this_vehicle, area_of_impact_other_vehicle  FROM 'bigquery-public-data.nhtsa_traffic_fatalities.cevent_2015'
        LIMIT 100
        """


df = bq_assistant.query_to_pandas(QUERY)

s_code = df.groupby(['parametr_name'])['state_code'].count()
seq_of_event = df.groupby(['arithmetic_mean'])['sequence_of_events_name'].count()
area_this = df.groupby(['parametr_name'])['area_of_impact_this_vehicle'].count()
area_other = df.groupby(['parametr_name'])['area_of_impact_other_vehicle'].count()


trace1 = go.Scatter(
                        x = s_code.index,
                        y = seq_of_event.values
                        mode = 'lines'
                    )



trace2 = go.Pie(
                        x = seq_of_event.index,
                        y = area_this.values
                    )

trace3 = go.Bar(
                        x = s_code.index,
                        y = area_other.values
)

data = [trace1]

layout = dict(
              title = '',
              xaxis= dict(title= ''),
              yaxis=dict(title=''),
             )
fig = dict(data = [trace1], layout = layout)
plot(fig)
