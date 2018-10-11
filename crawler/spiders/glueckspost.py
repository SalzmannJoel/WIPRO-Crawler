import scrapy
from scrapy.crawler import CrawlerProcess


class GlueckspostSpider(scrapy.Spider):
    name = "glueckspost"

    def start_requests(self):
        urls = [
            'https://www.glueckspost.ch/sternzeichen/wochenhoroskop-widder/',
            'https://www.glueckspost.ch/sternzeichen/wochenhoroskop-stier/',
            'https://www.glueckspost.ch/sternzeichen/wochenhoroskop-zwillinge/',
            'https://www.glueckspost.ch/sternzeichen/wochenhoroskop-krebs/',
            'https://www.glueckspost.ch/sternzeichen/wochenhoroskop-loewe/',
            'https://www.glueckspost.ch/sternzeichen/wochenhoroskop-jungfrau/',
            'https://www.glueckspost.ch/sternzeichen/wochenhoroskop-waage/',
            'https://www.glueckspost.ch/sternzeichen/wochenhoroskop-skorpion/',
            'https://www.glueckspost.ch/sternzeichen/wochenhoroskop-schuetze/',
            'https://www.glueckspost.ch/sternzeichen/wochenhoroskop-steinbock/',
            'https://www.glueckspost.ch/sternzeichen/wochenhoroskop-wassermann/',
            'https://www.glueckspost.ch/sternzeichen/wochenhoroskop-fische/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        sign = (response.url.split("/")[-2]).split("-")[-1]
        # alternativeSign = response.css("div.layout-element-horoscope .starsign h1.starsign-name").extract_first()
        horoskoptext = response.css("div.layout-element-horoscope .content>p:first-of-type::text").extract_first()
        with open("glueckspostHoroskops.txt", "a", encoding="utf-8") as horoskopfile:
            horoskopfile.write(sign)
            horoskopfile.write(":")
            horoskopfile.write(horoskoptext)
            horoskopfile.write("\n")
