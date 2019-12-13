import plotly.graph_objs as go
from plotly.offline import plot
from math import sin
import numpy as np

x = np.linspace(-3, 3, 100)
y = list (map( lambda t:t*t, x))


trace1 = go.Scatter(
                        x = x,
                        y = y,
                        mode = "lines",
                    )

fig = dict(data = [trace1])
plot(fig)

y = list (map( lambda t:sin(t), x))
trace2 = go.Scatter(
                        x = x,
                        y = y,
                        mode = "lines",
                        name="sin(t)",
                        marker=dict(color='rgba(80, 26, 80, 0.8)'),
                    )

fig = dict(data = [trace1,trace2])
plot(fig)


y = list (map( lambda t: abs(t), x))
trace3 = go.Scatter(
                        x = x,
                        y = y,
                        mode = "lines",
                        name="|x|",
                        marker=dict(color='rgba(80, 26, 80, 0.8)'),
                    )

layout = dict(
              title = 'x^2 and sin(t) and |x|',
              xaxis = dict(
                            title= 'x'
                           ),
              yaxis = dict(
                            title='y',

                           )
            )

fig = dict(data = [trace1,trace2,trace3], layout = layout)
plot(fig)

