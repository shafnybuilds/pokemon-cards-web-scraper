import logging
import re

import scrapy
from pokedex_scraper.items import PokedexEntry
from scrapy.http import HtmlResponse

# logging for internal debug printing
logger = logging.getLogger(__name__)


# initialize the spider
class PokedexSpider(scrapy.Spider):
    name = "pokedex_spider"

    start_urls = ["https://pokemondb.net/static/sitemaps/pokemondb.xml"]

    custom_settings = {
        "ITEM_PIPELINES": {"pokedex_scraper.piplines.PokedexPipeline": 300}
    }

    def parse(self, response):
        logger.debug("Extracting URLs from sitemap:XML")

        # defining a namespace mapping for XML parsing
        ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        urls = response.xpath("//s:url/s:loc/text()", namespaces=ns).getall()

        # for this use case, i have to scrape: https:pokemondb.net/charizard
        for url in urls:
            if re.match(r"^https://pokemondb\.net/pokedex/[^/]+$", url):
                yield scrapy.Request(url=url, callback=self.parse_pokemon)

    def parse_pokemon(self, response: HtmlResponse):
        response.xpath(
            '//main[@id="main" and contains(@class, "main-content") and contains(@class, "grid-container")]'
        ).get()

        # select all direct children of <main> and exclude <nav>
        content_parts = response.xpath(
            '//main[@id="main" and contains(@class, "main-content") and contains(@class, "grid-container")]/*[not(self::nav)]'
        ).getall()

        # join this to one HTML string
        cleaned_html = "".join(content_parts)

        pokemon_name = response.url.split("/")[-1]

        yield PokedexEntry(
            pokemon_name=response.url.split("/")[-1],
            url=response.url,
            html=cleaned_html,
        )
