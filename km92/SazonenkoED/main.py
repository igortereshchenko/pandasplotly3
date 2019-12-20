import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keys.json"

from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot

bq_assistant = BigQueryHelper('bigquery_public_data', 'nhtsa_traffic_fatalities')

QUERY = """
        SELECT state_number, vehicle_number, consecutive_number, driver_maneuvered_to_avoid_name FROM `bigquery-public-data.nhtsa_traffic_fatalities.maneuver_2016`
        LIMIT 10000
        """
df = bq_assistant.query_to_pandas(QUERY)

print(df)


reason_groupby = df.groupby(['driver_maneuvered_to_avoid_name'])['state_number'].count()

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
