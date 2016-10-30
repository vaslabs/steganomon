import json

def getPokemonTypes():
	with open('pokemon_data.json') as json_data:
		d = json.load(json_data)
		return d

pokemonTypes = getPokemonTypes()

def getPokemonTypesFromPokemonName(pokemonName):
    global pokemonTypes
    for entry in pokemonTypes:
	    if (entry["name"] == pokemonName):
		    return entry['types']