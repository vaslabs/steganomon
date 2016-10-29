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

