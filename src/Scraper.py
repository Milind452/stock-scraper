import requests
from bs4 import BeautifulSoup

class Scraper:
	def __init__(self, url):
		self.url = url

	def getHtml(self):
		return requests.get(self.url)

	def getSoup(self):
		return BeautifulSoup(self.getHtml().content, 'html.parser')

	def getTitle(self):
		return self.getSoup().title.text

	def getHead(self):
		return self.getSoup().head.text

	def getBody(self):
		return self.getSoup().body.text

	def getAllTables(self):
		return self.getSoup().find_all('table')

	def getTableByIndex(self, index, asDict = True):
		tables = self.getSoup().find_all('table')[index].text
		if not asDict:
			return tables

		tables = self.getAllTables()[index]
		results = dict()
		for row in tables.find_all('tr'):
			data = row.findAll('td')
			if data == []:
				continue
			results[data[0].text] = [element.text for element in data[1:]]

		return results

	def getAllAnchors(self):
		return self.getSoup().select('a')

if __name__ == '__main__':
	scraper = Scraper("https://www.moneycontrol.com/stocksmarketsindia/")
	# print(scraper.getTitle())
	# print('**************************')
	# print(scraper.getHead())
	# print('**************************')
	# print(scraper.getBody())
	# print(scraper.getAllTables())
	# print(scraper.getAllAnchors())
	print(scraper.getTableByIndex(1))

