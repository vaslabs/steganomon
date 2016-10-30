import json
import random


def getdata():
    with open('tm_data.json') as json_data:
        d = json.load(json_data)
        return d

def get_extended_data():
    with open('tm_data_extended.json') as json_data:
        d = json.load(json_data)
        return d

def getmap():
    numbers1 = []
    numbers2 = []
    numbers3 = []
    for num in range(1, 101):
        if (num % 3 == 0):
            numbers3.append(num)
        elif (num % 2 == 0):
            numbers2.append(num)
        else:
            numbers1.append(num)
    map = []
    map.append(numbers1)
    map.append(numbers2)
    map.append(numbers3)
    return map




data = getdata()
map = getmap()

data_extended = get_extended_data()


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

def get_any_attack(multiplier):
    global map
    return random.choice(map[multiplier-1])


def get_type_by_id(id):
    global data_extended
    for entry in data_extended:
        keyint = int(entry['id'])
        if (keyint == id):
            return type


def get_any_attack_with_types(multiplier, types):
    global map
    for try_number in range(1, 11):
        choice = random.choice(map[multiplier-1])
        choice_type = get_type_by_id(choice)
        if choice_type in types or choice_type == 'Normal':
            return choice
    return random.choice(map[multiplier-1])


