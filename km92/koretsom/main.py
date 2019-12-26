import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keys.json"

import pandas as pd
from bq_helper import BigQueryHelper
import plotly.graph_objs as go
from plotly.offline import plot

bq_assistant = BigQueryHelper('bigquery-public-data','nhtsa_traffic_fatalities')


QUERY = """
        SELECT day_of_week,day_of_crash,number_of_drunk_drivers,functional_system
        FROM `bigquery-public-data.nhtsa_traffic_fatalities.accident_2015`
        LIMIT 100
        """


df = bq_assistant.query_to_pandas(QUERY)

print(df.head(100))


trace1 = go.Scatter(
    x = list(i for i in range(1,32)),
    y = [df.day_of_crash[df.day_of_crash==i].count() for i in range(1,32)],
    mode = "lines",
)
layout1 = go.Layout(
    title = "crash on a particular day of the month",
    xaxis = dict(title = "day on mounth"),
    yaxis = dict(title = "number of crash")
)

trace2 = go.Pie(
    # кругова діаграма, ця діаграма показує скільки відсотків дтп відбуваються з участі людини в стані алкогольного спяніння
    labels = ['grink_man','angrink_man'],
    values = [df.number_of_drunk_drivers[df.number_of_drunk_drivers==1].count(),df.number_of_drunk_drivers[df.number_of_drunk_drivers==0].count()]
)
layout2 = go.Layout(
    title = "crash with drink drivers",
)

trace3 = go.Bar(
    x = ['sunday','monday','tuesday','wensday','tharsday','friday','saturday'],
    y = [df.day_of_week[df.day_of_week==1].count(),df.day_of_week[df.day_of_week==2].count(),df.day_of_week[df.day_of_week==3].count(),df.day_of_week[df.day_of_week==4].count(),df.day_of_week[df.day_of_week==5].count(),df.day_of_week[df.day_of_week==6].count(),df.day_of_week[df.day_of_week==7].count()]
)
layout3 = go.Layout(
    # стопчикова діаграма, показує в який день тижня найбільше дтп
    title = "day of week",
    xaxis = dict(title = "day 0f week"),
    yaxis = dict(title = "number of crash")
)

data = [trace1]
layout = layout1
fig = dict(data = data, layout = layout)
plot(fig)