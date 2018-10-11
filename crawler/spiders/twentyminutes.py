import scrapy
from scrapy.crawler import CrawlerProcess


class TwentyMinutesSpider(scrapy.Spider):
    name = "twentyminutes"

    def start_requests(self):
        urls = [
            'https://www.20min.ch/leben/horoskop/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        horoskops = response.css("div.horoskop>div.detail>div.sign")
        for horoskop in horoskops:
            sign = horoskop.css("div.sign>div.signinfo>h1::text").extract_first()
            horoskoptext = horoskop.css("div.sign>p::text").extract_first()
            with open("twentyminutesHoroskops.txt", "a", encoding="utf-8") as horoskopfile:
                horoskopfile.write(sign)
                horoskopfile.write(":")
                horoskopfile.write(horoskoptext)
                horoskopfile.write("\n")
