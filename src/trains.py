import requests as r
import json

import api_key
base_url = 'http://lapi.transitchicago.com/api/1.0/ttpositions.aspx?key=' + \
    api_key.key + '&rt='
url_suffix = '&outputType=JSON'


def make_request_url(routes:list, verbose=True):
    route_str = ','.join(routes)
    url = base_url + route_str + url_suffix
    if verbose:
        print(url)
    return url

def get_json(routes:list) -> dict:
    url = make_request_url(routes, verbose=True)
    j = r.get(url).text
    return json.loads(j)

def parse_data(data:dict):
    """

    """
    base = data['ctatt']
    routes = base['route']
    print(f'len(routes): {len(routes)}')

    all_trains = {}
    for i, route in enumerate(routes):
        # print(f'{i}: {route}')
        route_trains = route.get('train')
        if route_trains:
            all_trains[route['@name']] = route_trains

    return all_trains
    

def select_features(trains:dict, keys:list):
    # returns a dict where k = line color, v = list of train dicts
    train_dicts = {}
    for name, trains in trains.items():
        # print(f'trains: {trains}')
        # print(f'{name}: {type(trains)}')
        try:
            ts = [{k: t.get(k) for k in keys} for t in trains]
        except AttributeError:
            pass

        train_dicts[name] = ts
    return train_dicts


def get_coords(routes):
    json = get_json(routes)
    trains = parse_data(json)
    features = ['lat', 'lon']
    trains = select_features(trains, features)
    return trains

if __name__ == "__main__":
    routes = ['red', 'blue', 'brn', 'g', 'org', 'p', 'pink', 'y']
    cs = get_coords(routes)
    print(cs)
