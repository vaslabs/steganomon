import json

def read_data():
	data_file = open('my_secret_message.dat')
	data = json.load(data_file)
	data_file.close()
	edges = []
	for letter_obj in data:
		for edge in letter_obj["edges"]:
			pair = [{'x':edge["x1"], 'y':edge['y1']}, {'x':edge['x2'], 'y':edge['y2']}]
			edges.append(pair)
	return edges

def read_story():
	story_file = open('story.json')
	data = json.load(story_file)
	story_file.close()
	return data



