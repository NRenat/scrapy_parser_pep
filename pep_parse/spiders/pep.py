import re

import scrapy
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = "pep"
    allowed_domains = ["peps.python.org"]
    start_urls = ["https://peps.python.org/"]

    def parse(self, response):
        links = response.xpath(
            '//a[contains(@class, "pep") and starts-with(@href, "pep-")]/@href'
        )

        for pep in links:
            yield response.follow(pep, callback=self.parse_pep)

    def parse_pep(self, response):
        title = response.css('h1.page-title::text').get()
        match = re.search(r'PEP (\d+) – (.+)', title)
        number = match.group(1)
        name = match.group(2)

        superseded_xpath = (
            '//dt[text()="Status"]/following-sibling::dd[1]//text()'
        )
        status = response.xpath(superseded_xpath).get()
        data = {
            'number': number,
            'name': name,
            'status': status
        }
        yield PepParseItem(data)
