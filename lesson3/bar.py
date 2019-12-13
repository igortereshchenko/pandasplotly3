import plotly.graph_objs as go
from plotly.offline import plot

bar = go.Bar(x=['Bob', 'Boba', 'Jane', 'Jack', 'Kate'], y = [17,18,19,21,12])

layout = go.Layout(
                   title=' students',
                   xaxis=dict(title='students'),
                   yaxis=dict( title='ages'),
)

fig = go.Figure(data=[bar], layout=layout)
plot(fig)