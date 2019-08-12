

import plotly.plotly as py
import plotly.graph_objs as go

labels = ['Nutrients.csv']

trace = go.Pie(labels=labels, values=values)

py.iplot([trace], filename='basic_pie_chart')
