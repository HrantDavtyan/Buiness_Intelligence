import plotly.graph_objs as go

labels = ['HTML/CSS','Python','SQL','Other']
values = [15,50,15,20]
trace = go.Pie(labels=labels, values=values)
data = [trace]
f1 = dict(data=data)