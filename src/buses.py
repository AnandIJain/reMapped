import requests as r
import api_key
import utils


BUS_ROOT = 'http://ctabustracker.com/bustime/api/v2/'
JSON_SUFFIX = '&format=json'


def routes(key:str=api_key.BUS_KEY) -> dict:
    url = BUS_ROOT + 'getroutes?key=' + key + JSON_SUFFIX
    j = utils.grab(url)
    return j


def vehicles_from_routes(routes:list, key:str=api_key.BUS_KEY):
    routes_str = '&rt=' + ','.join(routes)
    url = BUS_ROOT + 'getvehicles?key=' + key + JSON_SUFFIX + routes_str
    j = utils.grab(url)
    return j


def vehicles_from_id(vehicle_ids:list, key:str=api_key.BUS_KEY):
    vid_str = '&vid=' + ','.join(vehicle_ids)
    url = BUS_ROOT + 'getvehicles?key=' + key + JSON_SUFFIX + vid_str
    j = utils.grab(url)
    return j


def main():
    data = routes()
    print(f'routes: {data}')
    rts = [rt['rt'] for rt in data['bustime-response']['routes']]
    print(f'route_numbers : {rts}')
    first_ten = rts[:10]
    vehicles = vehicles_from_routes(rts)
    return vehicles


if __name__ == "__main__":
    ft = main()
    print(f'ft: {ft}')
