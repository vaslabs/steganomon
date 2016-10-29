import json

def read_data():
	data_file = open('my_secret_message.dat')
	data = json.load(data_file)
	data_file.close()
	edges = []
	letterEdges = []
	for letter_obj in data:
		for edge in letter_obj["edges"]:
			pair = [{'x':edge["x1"], 'y':edge['y1']}, {'x':edge['x2'], 'y':edge['y2']}]
			edges.append(pair)
		letterEdges.append(len(letter_obj["edges"]))
	return edges, letterEdges

def read_story():
	story_file = open('story.json')
	data = json.load(story_file)
	story_file.close()
	return data

def read_story_dec():
	story_file = open('story_dec.json')
	data = json.load(story_file)
	story_file.close()
	return data

