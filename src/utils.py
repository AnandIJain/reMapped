import requests as r
import api_key


def grab(url:str) -> dict:
    j = r.get(url).json()
    return j


def select_features(json_data:dict, keys:list):
    # returns a dict where k = line color, v = list of train dicts
    data_dicts = {}
    for name, data in json_data.items():
        try:
            ts = [{k: t.get(k) for k in keys} for d in data]
        except AttributeError:
            pass

        data_dicts[name] = ts
    return data_dicts

    