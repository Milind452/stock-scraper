import requests
from bs4 import BeautifulSoup

import JsonHandler

home = JsonHandler.getEndpoint('home')
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

# for table in soup.select('table'):
#     print(table)
#     print("****************************************")

table = soup.select('table')[1].text
print(type(table))