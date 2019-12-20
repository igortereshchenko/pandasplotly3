import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "keys.json"

import pandas as pd
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot

bq_assistant = BigQueryHelper('bigquery-public-data','nhtsa_traffic_fatalities')

QUERY = """
        SELECT state_number, consecutive_number, driver_distracted_by, driver_distracted_by_name FROM `bigquery-public-data.nhtsa_traffic_fatalities.distract_2015`
        LIMIT 10000
        """

df = bq_assistant.query_to_pandas(QUERY)


# Задание1  Бары с невнимательными товарищами


low_attention = df.groupby(['state_number']).count()

bar = go.Bar(
    x = df.state_number,
    y = low_attention,

)

bar_layout = go.Layout(
    title = 'Количество смертей по невнимательности в разных штатах',
    xaxis = dict(title='Штаты'),
    yaxis = dict(title='Смерти'),

)

my_bar = go.Figure(data=[bar],layout = bar_layout)
plot(my_bar)