import csv

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of data.
filename = '/home/riya/Documents/Python/Python_projects/DataViz/json_data_plot/data/world_fires_1_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    lats, lons, brs = [], [], []
    for row in reader:
        lat = float(row[0])
        lon = float(row[1])
        br = float(row[2])
        lats.append(lat)
        lons.append(lon)
        brs.append(br)


# Map the fires.
# data = [Scattergeo(lon=lons, lat=lats)]
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        'size': [((br-300)/10) for br in brs],
        'color': brs,
        'colorscale': 'Rainbow',
        'reversescale': False,
        'colorbar': {'title': 'Brightness'},
    },
}]
my_layout = Layout(title="World Fires")

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='world_fires.html')