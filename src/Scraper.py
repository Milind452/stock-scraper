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

	def getTableByAttribute(self, attribute, asDict = True):
		tables = self.getSoup().find('table', attrs = attribute).text
		if not asDict:
			return tables

		tables = self.getSoup().find('table', attrs = attribute)
		results = dict()
		for row in tables.find_all('tr'):
			data = row.findAll('td')
			if data == []:
				continue
			results[data[0].text] = [element.text for element in data[1:]]
		return results

	def getAllAnchors(self):
		return self.getSoup().find_all('a')

	def getAnchorByIndex(self, index, asText = True):
		anchor =  self.getAllAnchors()[index]
		if not asText:
			return anchor
		return anchor.text

	def getAnchorByAttribute(self, attribute, asText = True):
		anchor =  self.getSoup().find('a', attribute)
		if not asText:
			return anchor
		return anchor.text

	def getAllDivs(self):
		return self.getSoup().find_all('div')

	def getDivByIndex(self, index, asText = True):
		pass

	def getDivByAttribute(self, attribute, astext = True):
		pass


if __name__ == '__main__':
	scraper = Scraper("https://www.moneycontrol.com/stocksmarketsindia/")
	# print(scraper.getAllTables())
	# print(scraper.getTableByIndex(1), False)
	# print(scraper.getTableByAttribute({'class' : 'mctable1'}))
	# print(scraper.getAllAnchors())
	# print(scraper.getAnchorByIndex(10, False))
	# print(scraper.getAnchorByAttribute({'title' : 'Personal Tech'}))
	print(scraper.getAllDivs())

