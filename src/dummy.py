import Scraper
import JsonHandler

url = JsonHandler.getJsonItem('home', '/../resources/endpoints.json')
scraper = Scraper.Scraper(url)
indianIndices = scraper.getTableByIndex(1)
globalIndices = scraper.getTableByIndex(2)
mostActiveStocks = scraper.getTableByIndex(3)
activityFiiAndDii = scraper.getTableByIndex(4)
activityFiiAndDii_2 = scraper.getTableByIndex(5)
topGainers = scraper.getTableByIndex(6)
topLosers = scraper.getTableByIndex(7)
onlyBuyers = scraper.getTableByIndex(9)
onlySellers = scraper.getTableByIndex(10)
weekHigh52 = scraper.getTableByIndex(12)
weekLow52 = scraper.getTableByIndex(14)
priceShockers = scraper.getTableByIndex(16)
volumeShockers = scraper.getTableByIndex(18)
intradayLargeDeals = scraper.getTableByIndex(19)

print(indianIndices)
print(globalIndices)
JsonHandler.setJsonObject(indianIndices, "/../target/IndianIndices.json")
JsonHandler.setJsonObject(indianIndices, "/../target/GlobalIndices.json")
