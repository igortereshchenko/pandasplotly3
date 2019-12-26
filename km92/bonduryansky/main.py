import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/Student/Desktop/Bonduryansky/pandasplotly3/keys.json"
import pandas
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot
bq_assistant = BigQueryHelper('bigquery_public_data', 'nhtsa_traffic_fatalities')

QUERY = """
        SELECT 'state_number', 'consecutive_number', 'vehicle_number', 'person_number' 
        FROM 'bigquery_public_data.nhtsa_traffic_fatalities.nmcrash_2016'
        LIMIT 10

        """
df =  bq_assistant.query_to_pandas(QUERY)
new_df = df.groupby(['state_number'])['vehicle_number']

df_state_car = nenew_df.sum

scatter1 = go.Scatter(
    x = df_state_car.index(),
    y = df_people_vehicles.index(),
    mode = "lines"
    )
layout = go.Layout(
    title = 'People on different cases in varying states'
)
figure1 = go.Figure(data = [scatter1], layout = layout)
plot(figure1)
