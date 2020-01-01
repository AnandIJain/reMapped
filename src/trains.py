import requests as r
import api_key
import utils

TRAIN_ROOT = 'http://lapi.transitchicago.com/api/1.0/'
TRAIN_URL = TRAIN_ROOT + 'ttpositions.aspx?key=' + api_key.TRAIN_KEY + '&rt='

JSON_SUFFIX = '&outputType=JSON'



def make_request_url(routes:list, verbose=True):
    # i think that for both trains and busses the maximum number of routes is 10

    route_str = ','.join(routes)
    url = base_url + route_str + JSON_SUFFIX

    if verbose:
        print(url)

    return url


def parse_train_data(data:dict):
    """

    """
    base = data['ctatt']
    routes = base['route']
    print(f'len(routes): {len(routes)}')

    all_trains = {}
    for i, route in enumerate(routes):
        route_trains = route.get('train')
        if route_trains:
            all_trains[route['@name']] = route_trains

    return all_trains


def get_coords(routes:list, output='dict'):
    # output is either 'df' or 'dict'
    url = make_request_url(routes, verbose=True)
    json = utils.grab(url)
    trains = parse_train_data(json)
    features = ['lat', 'lon']
    trains = utils.select_features(trains, features)

    if output == 'df':
        trains = pd.DataFrame.from_dict(trains, orient='index')
        
    return trains


def main():
    routes = ['red', 'blue', 'brn', 'g', 'org', 'p', 'pink', 'y']
    cs = get_coords(routes)
    return cs


if __name__ == "__main__":
    cs = main()
    print(cs)
