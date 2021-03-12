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


if __name__ == '__main__':
	scraper = Scraper("https://www.moneycontrol.com/stocksmarketsindia/")
	# print(scraper.getTitle())
	# print('**************************')
	# print(scraper.getHead())
	# print('**************************')
	# print(scraper.getBody())
	# print(scraper.getAllTables())

