import json


def getdata():
    with open('tm_data.json') as json_data:
        d = json.load(json_data)
        return d


def get_by_name(name):
    data = getdata()
    for key, value in data.items():
        if (key == name):
            return key, value


def get_by_id(id):
    data = getdata()
    for key, value in data.items():
        if (value == id):
            return key, value