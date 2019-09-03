import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd

# Plots each crime on a map of Los Angeles

plotly.tools.set_credentials_file(username='smoorjani', api_key='ZNLECT9fuPKYvIqUfd1M')

mapbox_access_token = 'pk.eyJ1Ijoic2FtcmFqbSIsImEiOiJjanFsNnpnMWEwaW83NDJxajE5a3VwYWk1In0.5ieoEoWVw4B_xcB8Mi68RA'

df = pd.read_csv('minimized.csv')

#lat_lon = list(df['Location '])
#df.dropna(subset=['Location '])
import random

lat_lon = list(map(lambda x: x[1:-1].replace(',',''),list(map(str,list(df['Location '])))))
lat_lon = list(filter(None, lat_lon))
lat_lon = random.sample(lat_lon, 40000)
#print(lat_lon[0])
lats = [float(str(a)[:a.find(' ')]) for a in lat_lon]
'''
counter = 0
for a in lat_lon:
    #print (counter)
    a = float(str(a)[:a.find(' ')])
    counter += 1
'''
lons = [float(str(a)[a.find(' ')+1:]) for a in lat_lon]
codes = list(df['Crime Code Description'])


data = [
    go.Scattermapbox(
        lat=lats,
        lon=lons,
        mode='markers',
        marker=dict(
            size=9
        ),
        text=codes,
    )
]

layout = go.Layout(
    autosize=True,
    hovermode='closest',
    mapbox=dict(
        accesstoken=mapbox_access_token,
        bearing=0,
        center=dict(

            lat=33.9829,
            lon=-118.3338
        ),
        pitch=0,
        zoom=10
    ),
)

fig = dict(data=data, layout=layout)
py.iplot(fig, filename='Multiple Mapbox')

