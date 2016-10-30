#!/usr/bin/python
from pokemonNames.pokemonNames import PokemonNames
import random as Random
import json
from random import random
pokemonNames = PokemonNames()

def generatePokemonIndex():
	pokemonIndexDict = {}
	for i in range(1,150):
		pokemonIndexDict[pokemonNames.get_name(i)] = i

	return pokemonIndexDict

pokemonIndex = generatePokemonIndex()


def getPokemonMap():
    numbers1 = []
    numbers2 = []
    numbers3 = []
    for num in range(1, 148):
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


pokemonMap = getPokemonMap()

def getPokemon(multiplier):
	global pokemonMap
	pokemonId = Random.choice(pokemonMap[multiplier - 1])
	pokemonOption1 = pokemonNames.get_name(pokemonId)
	return pokemonOption1

def getPokemonIndex(pokemonName):
	if (not pokemonName in pokemonIndex):
		return 0
	return pokemonIndex[pokemonName]



attack_descriptions = {
	"attacking":"{0} uses {1} on {2}",
	"defending" : "{0} used {1}"
}

trainer_descriptions = {
	"pokeball" : "{0} throws pokeball",
	"chooses_pokemon" : "{0}: {1}, I choose you!",
	"chooses_2_pokemon" : "{0}: {1}, {2}, I choose you!",
	"pokemon_return" : "{0}: {1} return!",
	"challenge" : "{0} challenges {1} to battle!"
}

passive_descriptions  = {
	"damage" : "{0} took {1} damage",
	"neutral" : "{0} is watching carefully",
	"caught" : "{0} was caught",
	"break_out" : "{0} broke out from the pokeball",
	"escape" : "{0} fled!",
	"faint":"{0} fainted!",
	"angry":"{0} is angry!",
	"strength" : "{0} is STRONG"
}

trainers = [
	"Gary", "Ash", "Green", "Red"
]
