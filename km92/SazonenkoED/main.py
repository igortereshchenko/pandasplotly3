import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keys.json"

from bq_helper import BigQueryHelper
import plotly.express as px
import plotly.graph_objs as go
from plotly.offline import plot

bq_assistant = BigQueryHelper('bigquery_public_data', 'nhtsa_traffic_fatalities')

QUERY = """
        SELECT state_number, vehicle_number, consecutive_number, driver_maneuvered_to_avoid_name FROM `bigquery-public-data.nhtsa_traffic_fatalities.maneuver_2016`
        LIMIT 10000
        """
df = bq_assistant.query_to_pandas(QUERY)

# print(df)


reason_groupby = df.groupby(['driver_maneuvered_to_avoid_name'])['consecutive_number'].count()
state_groupby  = df.groupby(['state_number'])['vehicle_number'].count()
print(reason_groupby)


# ---------- bar plot ----------
fig2 = {
  "data": [
    {
      "y": reason_groupby.values,
      "x": reason_groupby.index,
      "name": "reasons of fatalities",
      "type": "bar"
    },
  ],
  "layout": {
        "title":"reasons of fatalities",
    }
}
plot(fig2)


# ---------- pie plot ----------
fig = px.pie(df, values=reason_groupby.values, names=reason_groupby.index)
plot(fig)


# ----------scatter plot ----------
trace1 = go.Scatter(
                    x = state_groupby.index,
                    y = state_groupby.values,
                    mode = "lines+markers",
                    name = "fatalities"
                    )

layout = dict(title = 'fatalities',
              xaxis= dict(title= 'reasons'),
              yaxis=dict(title='states'))
fig3 = dict(data = trace1, layout = layout)
plot(fig3)