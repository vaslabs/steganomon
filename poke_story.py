#!/usr/bin/python
from steganomon_data import *
from random import random
from tm import get_any_attack, get_name_by_id, get_any_attack_with_types
from pokemon import getPokemonTypesFromPokemonName

trainerIndexes = []

letterLengthCounter = 0
letterLengths = []
letterPointer = 0

def generateStory(letterPoints, ll):
	global letterLengths, letterLengthCounter, letterPointer
	letterLengths = ll
	storyStarted = False;
	messages = []
	for letterPointPair in letterPoints:
		if (not storyStarted):
			messages.append(startingPoint())
			storyStarted = True
			choosePokemon(letterPointPair, messages)
		
		else:
			attack_first(messages, letterPointPair)
			attack_second(messages, letterPointPair)
			letterLengthCounter+=1
			if (letterLengthCounter >= letterLengths[letterPointer]):
				letterLengthCounter = 0
				letterPointer+=1
				addRandomSentence(messages)
	decideWinner(messages)
	return messages


def addRandomSentence(messages):
	modes = ["angry", "strength"]
	chosenMode = int(round(random()*len(modes)-1))
	trainerName = trainers[trainerIndexes[int(random())]]
	message = passive_descriptions[modes[chosenMode]].format(trainerName)
	messages.append({'trainer':trainerName, 'message':message})

def startingPoint():
	trainer1Index = int(round(random()*3))
	otherTrainerIndex = int(round(random()*3))
	while (trainer1Index == otherTrainerIndex):
		otherTrainerIndex = int(round(random()*3))
	global trainerIndexes 
	trainerIndexes = [trainer1Index, otherTrainerIndex]
	return {'trainer':trainers[trainer1Index], 'message':trainer_descriptions["challenge"].format(trainers[trainer1Index], trainers[otherTrainerIndex])}

pokemonInBattleTrainer1 = []
pokemonInBattleTrainer2 = []

pokemonLostFor1 = 0
pokemonLostFor2 = 0

def decideWinner(messages):
	if (pokemonLostFor1 > pokemonLostFor2):
		messages.append({'trainer':trainers[trainerIndexes[1]] , 'message':trainers[trainerIndexes[1]] + " won the fight"})
	elif (pokemonLostFor2 > pokemonLostFor1):
		messages.append({'trainer':trainers[trainerIndexes[0]] , 'message':trainers[trainerIndexes[0]] + " won the fight"})
	else:
		messages.append({'trainer':None, 'message':"Match ended in a DRAW"})

def choosePokemon(pointPair, messages):
	global trainerIndexes
	global pokemonInBattleTrainer1, pokemonInBattleTrainer2, letterLengthCounter
	firstPair = pointPair[0]
	secondPair = pointPair[1]
	firstPokemonIndex = firstPair["x"] + 1
	secondPokemonIndex = firstPair["y"] + 1
	firstPokemon = getPokemon(firstPokemonIndex)
	secondPokemon = getPokemon(secondPokemonIndex)
	pokemonInBattleTrainer1 = [firstPokemon, secondPokemon]
	trainerName = trainers[trainerIndexes[0]]
	messages.append({'trainer':trainerName, 'message':trainer_descriptions["chooses_2_pokemon"].format(trainerName, firstPokemon, secondPokemon)})

	firstPokemonIndex = secondPair["x"] + 1
	secondPokemonIndex = secondPair["y"] + 1
	firstPokemon = getPokemon(firstPokemonIndex)
	secondPokemon = getPokemon(secondPokemonIndex)
	pokemonInBattleTrainer2 = [firstPokemon, secondPokemon]
	trainerName = trainers[trainerIndexes[1]]
	messages.append({'trainer':trainerName, 'message':trainer_descriptions["chooses_2_pokemon"].format(trainerName, firstPokemon, secondPokemon)})
	letterLengthCounter+=1

def removeFromList(pokemonName, pokeList):
	pokeList.remove(pokemonName)

def attack_first(messages, letterPointPair):
	firstFaints = random() < 0.1
	secondFaints = random() < 0.1
	nextAttackIndexOfFirstPokemon = letterPointPair[0]["x"] + 1
	nextAttackIndexOfSecondPokemon = letterPointPair[0]["y"] + 1
	global pokemonInBattleTrainer1, pokemonInBattleTrainer2, pokemonLostFor1

	pokemonTargetIndex = int(random())
	pokemonAttackingName = pokemonInBattleTrainer1[0]
	trainerName = trainers[trainerIndexes[0]]
	if (firstFaints):
		messages.append({'trainer':trainerName, 'message':passive_descriptions["faint"].format(pokemonAttackingName)})
		removeFromList(pokemonAttackingName, pokemonInBattleTrainer1)
		nextPokemon = getPokemon(nextAttackIndexOfFirstPokemon)
		messages.append({'trainer':trainerName, 'message':trainer_descriptions["chooses_pokemon"].format(trainerName, nextPokemon)})
		pokemonInBattleTrainer1.append(nextPokemon)
		pokemonLostFor1+=1
	else:
		pokemonTargetName = pokemonInBattleTrainer2[pokemonTargetIndex]
		pokemonTypes = getPokemonTypesFromPokemonName(pokemonAttackingName)
		attack = get_name_by_id(get_any_attack_with_types(nextAttackIndexOfFirstPokemon, pokemonTypes))
		messages.append({'trainer':trainerName, 'message':attack_descriptions["attacking"].format(pokemonAttackingName, attack, pokemonTargetName)})


	pokemonTargetName = pokemonInBattleTrainer2[pokemonTargetIndex-1]
	pokemonAttackingName = pokemonInBattleTrainer1[1]

	if (secondFaints):
		messages.append({'trainer':trainerName, 'message':passive_descriptions["faint"].format(pokemonAttackingName)})
		removeFromList(pokemonAttackingName, pokemonInBattleTrainer1)
		nextPokemon = getPokemon(nextAttackIndexOfSecondPokemon)
		messages.append({'trainer':trainerName, 'message':trainer_descriptions["chooses_pokemon"].format(trainers[trainerIndexes[0]], nextPokemon)})
		pokemonInBattleTrainer1.append(nextPokemon)
		pokemonLostFor1+=1
	else:
		pokemonTypes = getPokemonTypesFromPokemonName(pokemonAttackingName)
		attack = get_name_by_id(get_any_attack_with_types(nextAttackIndexOfSecondPokemon, pokemonTypes))
		messages.append({'trainer':trainerName, 'message':attack_descriptions["attacking"].format(pokemonAttackingName, attack, pokemonTargetName)})

def attack_second(messages, letterPointPair):
	firstFaints = random() < 0.1
	secondFaints = random() < 0.1
	nextAttackIndexOfFirstPokemon = letterPointPair[1]["x"] + 1
	nextAttackIndexOfSecondPokemon = letterPointPair[1]["y"] + 1
	global pokemonInBattleTrainer1, pokemonInBattleTrainer2, pokemonLostFor2
	pokemonTargetIndex = int(random())
	pokemonTargetName = pokemonInBattleTrainer1[pokemonTargetIndex]
	pokemonAttackingName = pokemonInBattleTrainer2[0]
	trainerName = trainers[trainerIndexes[1]]

	if (firstFaints):
		messages.append({'trainer':trainerName, 'message':passive_descriptions["faint"].format(pokemonAttackingName)})
		removeFromList(pokemonAttackingName, pokemonInBattleTrainer2)
		nextPokemon = getPokemon(nextAttackIndexOfFirstPokemon)
		messages.append({'trainer':trainerName, 'message':trainer_descriptions["chooses_pokemon"].format(trainerName, nextPokemon)})
		pokemonInBattleTrainer2.append(nextPokemon)
		pokemonLostFor2+=1
	else:
		pokemonTypes = getPokemonTypesFromPokemonName(pokemonAttackingName)
		attack = get_name_by_id(get_any_attack_with_types(nextAttackIndexOfFirstPokemon, pokemonTypes))
		messages.append({'trainer':trainerName, 'message':attack_descriptions["attacking"].format(pokemonAttackingName, attack, pokemonTargetName)})

	pokemonTargetName = pokemonInBattleTrainer1[pokemonTargetIndex-1]
	pokemonAttackingName = pokemonInBattleTrainer2[1]

	if (secondFaints):
		messages.append({'trainer':trainerName, 'message':passive_descriptions["faint"].format(pokemonAttackingName)})
		removeFromList(pokemonAttackingName,pokemonInBattleTrainer2)
		nextPokemon = getPokemon(nextAttackIndexOfSecondPokemon)
		messages.append({'trainer':trainerName, 'message':trainer_descriptions["chooses_pokemon"].format(trainers[trainerIndexes[1]], nextPokemon)})
		pokemonInBattleTrainer2.append(nextPokemon)
		pokemonLostFor2+=1
	else:
		pokemonTypes = getPokemonTypesFromPokemonName(pokemonAttackingName)
		attack = get_name_by_id(get_any_attack_with_types(nextAttackIndexOfSecondPokemon, pokemonTypes))
		messages.append({'trainer':trainerName, 'message':attack_descriptions["attacking"].format(pokemonAttackingName, attack, pokemonTargetName)})





