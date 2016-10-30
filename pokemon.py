import json
from steganomon_data import getPokemonIndex

def getPokemonTypes():
	with open('pokemon_data.json') as json_data:
		d = json.load(json_data)
		return d

pokemonTypes = getPokemonTypes()

def getPokemonTypesFromPokemonName(pokemonName):
    global pokemonTypes
    for entry in pokemonTypes:		
        if (int(entry["id"]) == getPokemonIndex(pokemonName)):
			return entry['types']