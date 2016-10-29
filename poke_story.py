#!/usr/bin/python
from steganomon_data import *
from random import random
from tm import get_any_attack, get_name_by_id

trainerIndexes = []

def generateStory(letterPoints):
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


	print messages



def startingPoint():
	trainer1Index = int(round(random()*3))
	otherTrainerIndex = int(round(random()*3))
	while (trainer1Index == otherTrainerIndex):
		otherTrainerIndex = int(round(random()*3))
	global trainerIndexes 
	trainerIndexes = [trainer1Index, otherTrainerIndex]
	return trainer_descriptions["challenge"].format(trainers[trainer1Index], trainers[otherTrainerIndex])

pokemonInBattleTrainer1 = []
pokemonInBattleTrainer2 = []

def choosePokemon(pointPair, messages):
	global trainerIndexes
	global pokemonInBattleTrainer1, pokemonInBattleTrainer2
	firstPair = pointPair[0]
	secondPair = pointPair[1]
	firstPokemonIndex = firstPair["x"] + 1
	secondPokemonIndex = firstPair["y"] + 1
	firstPokemon = pokemonNames.get_name(firstPokemonIndex)
	secondPokemon = pokemonNames.get_name(secondPokemonIndex)
	pokemonInBattleTrainer1 = [firstPokemon, secondPokemon]
	trainerName = trainers[trainerIndexes[0]]
	messages.append(trainer_descriptions["chooses_2_pokemon"].format(trainerName, firstPokemon, secondPokemon))

	firstPokemonIndex = secondPair["x"] + 1
	secondPokemonIndex = secondPair["y"] + 1
	firstPokemon = pokemonNames.get_name(firstPokemonIndex)
	secondPokemon = pokemonNames.get_name(secondPokemonIndex)
	pokemonInBattleTrainer2 = [firstPokemon, secondPokemon]
	trainerName = trainers[trainerIndexes[1]]
	messages.append(trainer_descriptions["chooses_2_pokemon"].format(trainerName, firstPokemon, secondPokemon))


def attack_first(messages, letterPointPair):
	firstFaints = random() < 0.1
	secondFaints = random() < 0.1
	nextAttackIndexOfFirstPokemon = letterPointPair[0]["x"] + 1
	nextAttackIndexOfSecondPokemon = letterPointPair[0]["y"] + 1
	global pokemonInBattleTrainer1, pokemonInBattleTrainer2

	pokemonTargetIndex = int(random())
	pokemonAttackingName = pokemonInBattleTrainer1[0]

	if (firstFaints):
		messages.append(passive_descriptions["faint"].format(pokemonAttackingName))
		nextPokemon = pokemonNames.get_name(nextAttackIndexOfFirstPokemon)
		messages.append(trainer_descriptions["chooses_pokemon"].format(trainers[trainerIndexes[0]], nextPokemon))
	else:
		pokemonTargetName = pokemonInBattleTrainer2[pokemonTargetIndex]
		attack = get_name_by_id(get_any_attack(nextAttackIndexOfFirstPokemon))
		messages.append(attack_descriptions["attacking"].format(pokemonAttackingName, attack, pokemonTargetName))


	pokemonTargetName = pokemonInBattleTrainer2[pokemonTargetIndex-1]
	pokemonAttackingName = pokemonInBattleTrainer1[1]

	if (secondFaints):
		messages.append(passive_descriptions["faint"].format(pokemonAttackingName))
		nextPokemon = pokemonNames.get_name(nextAttackIndexOfSecondPokemon)
		messages.append(trainer_descriptions["chooses_pokemon"].format(trainers[trainerIndexes[0]], nextPokemon))
	else:
		attack = get_name_by_id(get_any_attack(nextAttackIndexOfSecondPokemon))
		messages.append(attack_descriptions["attacking"].format(pokemonAttackingName, attack, pokemonTargetName))

def attack_second(messages, letterPointPair):
	firstFaints = random() < 0.1
	secondFaints = random() < 0.1
	nextAttackIndexOfFirstPokemon = letterPointPair[1]["x"] + 1
	nextAttackIndexOfSecondPokemon = letterPointPair[1]["y"] + 1
	global pokemonInBattleTrainer1, pokemonInBattleTrainer2
	pokemonTargetIndex = int(random())
	pokemonTargetName = pokemonInBattleTrainer1[pokemonTargetIndex]
	pokemonAttackingName = pokemonInBattleTrainer2[0]
	
	if (firstFaints):
		messages.append(passive_descriptions["faint"].format(pokemonAttackingName))
		nextPokemon = pokemonNames.get_name(nextAttackIndexOfFirstPokemon)
		messages.append(trainer_descriptions["chooses_pokemon"].format(trainers[trainerIndexes[1]], nextPokemon))
	else:
		attack = get_name_by_id(get_any_attack(nextAttackIndexOfFirstPokemon))
		messages.append(attack_descriptions["attacking"].format(pokemonAttackingName, attack, pokemonTargetName))

	pokemonTargetName = pokemonInBattleTrainer1[pokemonTargetIndex-1]
	pokemonAttackingName = pokemonInBattleTrainer2[1]

	if (secondFaints):
		messages.append(passive_descriptions["faint"].format(pokemonAttackingName))
		nextPokemon = pokemonNames.get_name(nextAttackIndexOfSecondPokemon)
		messages.append(trainer_descriptions["chooses_pokemon"].format(trainers[trainerIndexes[1]], nextPokemon))
	else:
		attack = get_name_by_id(get_any_attack(nextAttackIndexOfSecondPokemon))
		messages.append(attack_descriptions["attacking"].format(pokemonAttackingName, attack, pokemonTargetName))





