#!/usr/bin/python
from poke_story import generateStory
from poke_utils import read_data
import json
story_points = read_data()
messages = generateStory(story_points)
print json.dumps(messages)