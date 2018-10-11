import scrapy
from scrapy.crawler import CrawlerProcess


class ManticusSpider(scrapy.Spider):
    name = "manticus"

    def start_requests(self):
        urls = [
            'https://www.manticus.ch/tages-horoskop-aries',
            'https://www.manticus.ch/tages-horoskop-taurus',
            'https://www.manticus.ch/tages-horoskop-gemini',
            'https://www.manticus.ch/tages-horoskop-cancer',
            'https://www.manticus.ch/tages-horoskop-leo',
            'https://www.manticus.ch/tages-horoskop-virgo',
            'https://www.manticus.ch/tages-horoskop-libra',
            'https://www.manticus.ch/tages-horoskop-scorpio',
            'https://www.manticus.ch/tages-horoskop-sagittarius',
            'https://www.manticus.ch/tages-horoskop-capricorn',
            'https://www.manticus.ch/tages-horoskop-aquarius',
            'https://www.manticus.ch/tages-horoskop-pisces'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        sign = response.css("div#horoscope-detail>.contents>h2>span::text").extract_first()
        horoskoptext = response.css("div#horoscope-detail>.contents>.wink>.content::text").extract_first()
        with open("manticusHoroskops.txt", "a", encoding="utf-8") as horoskopfile:
            horoskopfile.write(sign)
            horoskopfile.write(":")
            horoskopfile.write(horoskoptext)
            horoskopfile.write("\n")
