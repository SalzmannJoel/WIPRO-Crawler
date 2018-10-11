import scrapy
from scrapy.crawler import CrawlerProcess


class AstroportalSpider(scrapy.Spider):
    name = "astroportal"

    def start_requests(self):
        urls = [
            'https://www.astroportal.com/tageshoroskope/widder/',
            'https://www.astroportal.com/tageshoroskope/stier/',
            'https://www.astroportal.com/tageshoroskope/zwillinge/',
            'https://www.astroportal.com/tageshoroskope/krebs/',
            'https://www.astroportal.com/tageshoroskope/loewe/',
            'https://www.astroportal.com/tageshoroskope/jungfrau/',
            'https://www.astroportal.com/tageshoroskope/waage/',
            'https://www.astroportal.com/tageshoroskope/skorpion/',
            'https://www.astroportal.com/tageshoroskope/schuetze/',
            'https://www.astroportal.com/tageshoroskope/steinbock/',
            'https://www.astroportal.com/tageshoroskope/wassermann/',
            'https://www.astroportal.com/tageshoroskope/fische/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        sign = response.url.split("/")[-2]
        horoskoptext = response.css("div#content>div>div>p:first-of-type::text").extract_first()
        with open("astroportalHoroskops.txt", "a", encoding="utf-8") as horoskopfile:
            horoskopfile.write(sign)
            horoskopfile.write(":")
            horoskopfile.write(horoskoptext)
            horoskopfile.write("\n")
