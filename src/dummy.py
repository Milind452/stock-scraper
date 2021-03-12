import Scraper
import JsonHandler

url = JsonHandler.getJsonItem('home', '/../resources/endpoints.json')
scraper = Scraper.Scraper(url)
indices = scraper.getTableByIndex(1)

print(indices)
JsonHandler.setJsonObject(indices, "/../target/indices.json")
