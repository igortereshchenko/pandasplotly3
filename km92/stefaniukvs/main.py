import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keys.json"

import pandas as pd
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot

bq_assistant = BigQueryHelper('bigquery-public-data','nhtsa_traffic_fatalities')


QUERY = """
        SELECT state_number, consecutive_number, driver_distracted_by, driver_distracted_by_name  
        FROM `bigquery-public-data.nhtsa_traffic_fatalities.distract_2015`
        LIMIT 100
        """


df = bq_assistant.query_to_pandas(QUERY)

print(df.head(9))
#df['']



trace1 = go.Scatter(

                    )



trace2 = go.Pie(

                    )

trace3 = go.Bar(


)

data = [trace1]

layout = dict(
              title = '',
              xaxis= dict(title= ''),
              yaxis=dict(title=''),
             )
fig = dict(data = [trace1], layout = layout)
plot(fig)
