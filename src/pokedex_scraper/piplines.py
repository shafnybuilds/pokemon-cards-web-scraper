import logging
import json
from pathlib import Path

import markdownify as md

from pokedex_scraper.items import PokedexEntry
from pokedex_scraper.spiders.pokedex_spider import PokedexSpider


logger = logging.getLogger(__name__)

