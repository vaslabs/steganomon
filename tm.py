import json


def getdata():
    with open('tm_data.json') as json_data:
        d = json.load(json_data)
        return d

data = getdata()


def get_by_name(name):
    global data
    for key, value in data.items():
        if (key == name):
            valueint = int(value)
            return key, valueint


def get_by_id(id):
    global data
    for key, value in data.items():
        valueint = int(value)
        if (valueint == id):
            return key, valueint


def get_name_by_id(id):
    global data
    for key, value in data.items():
        valueint = int(value)
        if (valueint == id):
            return key


def get_id_by_name(name):
    global data
    for key, value in data.items():
        if (key == name):
            valueint = int(value)
            return valueint


