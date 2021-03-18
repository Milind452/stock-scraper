import Scraper
import JsonHandler

url = JsonHandler.getJsonItem('home', '/../resources/endpoints.json')
scraper = Scraper.Scraper(url)
indianIndices = scraper.getTableByIndex(1)
globalIndices = scraper.getTableByIndex(2)

print(indianIndices)
print(globalIndices)
JsonHandler.setJsonObject(indianIndices, "/../target/IndianIndices.json")
JsonHandler.setJsonObject(indianIndices, "/../target/GlobalIndices.json")
