#!/usr/bin/python
from poke_story import generateStory
from poke_utils import read_data
import json
story_points, lengthOfEdges = read_data()
messages = generateStory(story_points, lengthOfEdges)
print json.dumps(messages)