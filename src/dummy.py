import requests
from bs4 import BeautifulSoup
import re

import JsonHandler

home = JsonHandler.getJsonItem('home', '/../resources/endpoints.json')
page = requests.get(home)
soup = BeautifulSoup(page.content, 'html.parser')

pageTitle = soup.title.text
pageHead = soup.head
pageBody = soup.body.text

# print(pageTitle)
# print("********************************")
# print(pageHead)
# print("********************************")
# print(pageBody)

table = soup.select('table')[1].text

table = list(table.split('\n'))
temp = list()
tmp = list()
counter = 1
for element in table:
    if element == '':
        continue
    tmp.append(element)
    if counter % 4 == 0:
        temp.append(tmp)
        tmp = list()
    counter += 1

indices = dict()
for x in range(1, len(temp)):
    indices[temp[x].pop(0)] = temp[x]

print(indices)
JsonHandler.setJsonObject(indices, "/../target/indices.json")
