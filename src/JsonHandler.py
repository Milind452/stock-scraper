import os
import json

def getCurrentWorkingDirectory():
	return os.path.dirname(os.path.realpath(__file__));

def getEndpoint():
	path = getCurrentWorkingDirectory() + '/../resources/endpoints.json'
	with open(path) as inputJson:
		endpoints = json.load(inputJson)
		return endpoints

print(getCurrentWorkingDirectory())
print(type(getEndpoint()), getEndpoint())
