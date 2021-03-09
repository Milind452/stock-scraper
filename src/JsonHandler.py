import os
import json

def getCurrentWorkingDirectory():
	return os.path.dirname(os.path.realpath(__file__));

def getAllEndpoints():
	path = getCurrentWorkingDirectory() + '/../resources/endpoints.json'
	with open(path) as inputJson:
		endpoints = json.load(inputJson)
		return endpoints

def getEndpoint(endpoint):
	endpointDict = getAllEndpoints()
	return endpointDict[endpoint]

# print(getCurrentWorkingDirectory())
# print(type(getAllEndpoints()), getAllEndpoints())
# print(getEndpoint("home"))
