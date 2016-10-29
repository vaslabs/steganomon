#!/usr/bin/python
from pokemonNames.pokemonNames import PokemonNames
from random import random
pokemonNames = PokemonNames()

def generatePokemonIndex():
	pokemonIndexDict = {}
	for i in range(1,151):
		pokemonIndexDict[pokemonNames.get_name(i)] = i

	return pokemonIndexDict

pokemonIndex = generatePokemonIndex()

def getPokemon(pokemonId, modulo):
	if pokemonId <= 0 or pokemonId > 151:
		return 'Missingno'
	pokemonOption1 = pokemonNames.get_name(pokemonId)
	nextPokemonIndex = pokemonId+modulo
	if (nextPokemonIndex > 148):
		return pokemonOption1
	pokemonOption2 = pokemonNames.get_name(nextPokemonIndex)
	if (random() < 0.5):
		return pokemonOption1
	return pokemonOption2

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
	"escape" : "{0} fled!"
}

trainers = [
	"Gary", "Ash", "Green", "Red"
]

attack_tms = [
	'Cut',
	'Razor leaf',
	'Flamethrower',
	'Watergun'	
]
