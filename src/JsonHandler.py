import os
import json

def getCurrentWorkingDirectory():
	return os.path.dirname(os.path.realpath(__file__))

def getJsonObject(relativePath):
	path = getCurrentWorkingDirectory() + relativePath
	with open(path) as inputJson:
		jsonObject = json.load(inputJson)
		return jsonObject

def getJsonItem(item, relativePath):
	jsonObject = getJsonObject(relativePath)
	return jsonObject[item]

def setJsonObject(jsonObject, relativePath):
	path = getCurrentWorkingDirectory() + relativePath
	with open(path, 'w') as outputJson:
		json.dump(jsonObject, outputJson)

# print(getCurrentWorkingDirectory())
# print(type(getJsonObject('/../resources/endpoints.json')), type(getJsonItem('home', '/../resources/endpoints.json')))
# print(getJsonObject('/../resources/endpoints.json'), getJsonItem('home', '/../resources/endpoints.json'))
