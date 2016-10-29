from poke_utils import read_story
from steganomon_data import getPokemonIndex
from tm import get_id_by_name
story = read_story()

def getRealIndex(index):
	if (index%3 == 0):
		index = 2
	elif index%2 == 0:
		index = 1
	else:
		index = 0
	return index

def readEntryPoint(entry):
	usefulParts = entry.split(':')[1].split(',')
	entryPokemon1 = usefulParts[0].strip()
	entryPokemon2 = usefulParts[1].strip()
	pokemon1RealIndex = getRealIndex(getPokemonIndex(entryPokemon1))

	firstPoint = {'x':pokemon1RealIndex, 'y':getRealIndex(getPokemonIndex(entryPokemon2))}
	return firstPoint

def isAttack(entryMessage):
	return ' uses ' in entryMessage

def parseAttackSentence(attackMessage):
	startFrom = attackMessage.index(' uses ') + 6
	endsAt = attackMessage.index(' on ')
	return attackMessage[startFrom:endsAt]

def isPokemonChoice(message):
	return ', I choose you!' in message

def parsePokemonNameInChoice(message):
	startIndex =message.index(': ') + 2
	endIndex = message.index(", I choose you!")
	return message[startIndex:endIndex]

def parseStory(story):
	firstPoint = readEntryPoint(story[1]["message"])
	secondPoint = readEntryPoint(story[2]["message"])
	print firstPoint, secondPoint,
	nextPoint={}
	for entry in story[3:]:
		message = entry["message"]
		if isAttack(message):
			attackName = parseAttackSentence(message)
			attackRealIndex = getRealIndex(get_id_by_name(attackName))
			if ('x' in nextPoint):
				nextPoint['y'] = attackRealIndex
				print nextPoint,
				nextPoint = {}
			else:
				nextPoint['x'] = attackRealIndex
		elif isPokemonChoice(message):
			pokemonName = parsePokemonNameInChoice(message)
			pokemonRealIndex = getRealIndex(getPokemonIndex(pokemonName))
			if ('x' in nextPoint):
				nextPoint['y'] = pokemonRealIndex
				print nextPoint,
				nextPoint = {}
			else:
				nextPoint['x'] = pokemonRealIndex			




parseStory(story)




