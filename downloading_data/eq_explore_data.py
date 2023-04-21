import json
from eq_world_map import WorldMap

class EarthQuakeAnalyser:
    def __init__(self, filename = 'eq_data/eq_data_1_day_m1.geojson'):
        self.filename = filename
    def explore (self):
        with open(self.filename) as f:
            all_eq_data = json.load(f)
        all_eq_dicts = all_eq_data['features']
        print(f'{len(all_eq_dicts)}')
        mags, lons, lats = [], [], []
        for eq_dict in all_eq_dicts:
            mag = eq_dict['properties']['mag']
            lon = eq_dict ['geometry']['coordinates'][0]
            lat = eq_dict['geometry']['coordinates'][1]
            mags.append(mag)
            lons.append(lon)
            lats.append(lat)
        print(f' Mags : {mags[:5]}')
        print(f' Mags : {lons[:5]}')
        print(f' Mags : {lats[:5]}')
        print(f'Max mags = {max(mags)}')
        WorldMap(lons,lats, mags)
        '''
        readable_file = 'eq_data/readable_eq_data.geojson'
        with open(readable_file, 'w') as f:
            #Read and write into the file
            json.dump(all_eq_data, f, indent=4)
        '''

eq = EarthQuakeAnalyser('eq_data/eq_data_30_day_m1.geojson')
eq.explore()
