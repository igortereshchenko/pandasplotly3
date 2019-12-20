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

print(df.head(10))

grink_man = df[df['number_of_drunk_drivers']=='1']
angrink_man = df[df['number_of_drunk_drivers']=='0']
#number_of_drunk_drivers = grink_man.groupby(angrink_man)

x = len(grink_man)
y = len(angrink_man)
labels = ['grink_man','angrink_man']
values = [15,4]
# fig = go.Figure(data=[go.Pie(labels = labels,values = values)])
# plot(fig)

bar = go.Bar(x = labels, y = values)
fig = go.Figure(data = [bar])



# trace1 = go.Scatter()
#
# trace2 = go.Pie()
#
# trace3 = go.Bar()
#
#
# data = [trace1]
#
# layout = dict(
#               title = '',
#               xaxis= dict(title= ''),
#               yaxis=dict(title=''),
#              )
# fig = dict(data = [trace1], layout = layout)
# plot(fig)
