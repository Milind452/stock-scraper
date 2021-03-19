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
		anchor =  self.getSoup().find('a', attrs = attribute)
		if not asText:
			return anchor
		return anchor.text

	def getAllDivs(self):
		return self.getSoup().find_all('div')

	def getDivByIndex(self, index, asText = True):
		div = self.getAllDivs()[index]
		if not asText:
			return div
		return div.text

	def getDivByAttribute(self, attribute, asText = True):
		div = self.getSoup().find('div', attrs = attribute)
		if not asText:
			return div
		return div.text

	def getAllSpans(self):
		return self.getSoup().find_all('span')

	def getSpanByIndex(self, index, asText = True):
		span = self.getAllSpans()[index]
		if not asText:
			return span
		return span.text

	def getSpanByAttribute(self, attribute, asText = True):
		span = self.getSoup().find('span', attrs = attribute)
		if not asText:
			return span
		return span.text

	def getAllUnorderedLists(self):
		return self.getSoup().find_all('ul')

	def getUnorderedListByIndex(self, index, asList = True):
		unorderedList = self.getAllUnorderedLists()[index]
		if not asList:
			return unorderedList
		results = list()
		for li in unorderedList.find_all('li'):
			if li == []:
				continue
			results.append(li.text.strip())
		return results

	def getUnorderedListByAttribute(self, attribute, asList = True):
		unorderedList = self.getSoup().find('ul', attrs = attribute)
		if not asList:
			return unorderedList
		results = list()
		for li in unorderedList.find_all('li'):
			if li == []:
				continue
			results.append(li.text.strip())
		return results

	def getAllOrderedLists(self):
		return self.getSoup().find_all('ol')

	def getOrderedListByIndex(self, index, asList = True):
		orderedList = self.getAllOrderedLists()[index]
		if not asList:
			return orderedList
		results = list()
		for li in orderedList.find_all('li'):
			if li == []:
				continue
			results.append(li.text.strip())
		return results

	def getOrderedListByAttribute(self, attribute, asList = True):
		orderedList = self.getSoup().find('ol', attrs = attribute)
		if not asList:
			return orderedList
		results = list()
		for li in orderedList.find_all('li'):
			if li == []:
				continue
			results.append(li.text.strip())
		return results



if __name__ == '__main__':
	scraper = Scraper("https://www.moneycontrol.com/stocksmarketsindia/")
	

