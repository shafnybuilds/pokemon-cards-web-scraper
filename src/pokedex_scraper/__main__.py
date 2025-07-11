import os

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from pokedex_scraper.spiders.pokedex_spider import PokedexSpider

os.environ["SCRAPY_SETTINGS_MODULE"] = "pokedex_scraper.settings"

if __name__ == "__main__":
    settings = get_project_settings()
    process = CrawlerProcess(settings=settings)
    process.crawl(PokedexSpider)
    process.start()