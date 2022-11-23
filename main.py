import pandas as pd
import plotly.express as px

df = pd.read_csv('Stars.csv')
starname = df['star_name'].tolist()
distance = df['distance'].tolist()
mass = df['distance'].tolist()
radius = df['radius'].tolist()
gravity = df['gravity'].tolist()

fig1 = px.bar(x=starname, y=mass, labels={'x': 'Starname', 'y': 'Mass'})
fig1.show()

fig2 = px.bar(x=starname, y=radius, labels={'x': 'Starname', 'y': 'Radius'})
fig2.show()

fig3 = px.bar(x=starname, y=distance, labels={
              'x': 'Starname', 'y': 'Distance'})
fig3.show()

fig4 = px.bar(x=starname, y=gravity, labels={'x': 'Starname', 'y': 'Gravity'})
fig4.show()
