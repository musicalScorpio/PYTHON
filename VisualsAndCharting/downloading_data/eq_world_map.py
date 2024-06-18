from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

class WorldMap :
    def __init__(self, lons, lats ,mags):
        #data = [Scattergeo(lon=lons, lat=lats)]
        data = [{
            'type': 'scattergeo',
            'lon': lons,
            'lat': lats,
             'marker': { 'size': [5 * mag for mag in mags],
                         'color': mags,'colorscale': 'Viridis','reversescale': True, 'colorbar': {'title': 'Magnitude'},

                         },
                }]
        my_layout = Layout(title='Global Earthquakes')
        fig = {'data': data, 'layout': my_layout}
        offline.plot(fig, filename='global_earthquakes.html')