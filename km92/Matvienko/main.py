import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keys.json"

import pandas as pd
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot

bq_assistant = BigQueryHelper(,)


QUERY = """
        SELECT year_of_crash,country,hour_of_crash,land_use  FROM "bigquery_public_data.nhtsa_traffic_fatalities.accident_2015"
        LIMIT 10
        """


df = bq_assistant.query_to_pandas(QUERY)
print(df.head(10))


trace1 = go.Scatter(
                    mode="lines"

                    )
layout1 = dict(
              title = "",
              xaxis= dict(title= ''),
              yaxis=dict(title=''),
             )
fig1 = dict(data = [trace1], layout = layout1)
plot(fig1)


year_of_crash=["year_of_crash"]
country=["country"]
trace2 = go.Pie(year_of_crash=values,
                country=labels
                    )
data = [trace2]
layout2 = dict(
              title = 'in which country is the most often occur crashes?',
              xaxis= dict(title= 'country'),
              yaxis=dict(title='land_use'),
             )
fig2 = dict(data = [trace2], layout = layout2)
plot(fig2)



land_use=df["land_use"]
country=df["country"]

data = [trace3]
layout3 = dict(
              title = 'in which location crashes occur most often?',
              xaxis= dict(title= 'country'),
              yaxis=dict(title='land_use'),
             )
trace3 = go.Bar((x=country,
                y=land_use,

)
fig3 = dict(data = [trace3], layout = layout3)
plot(fig3)

