import scrapy
from scrapy.crawler import CrawlerProcess


class GmxSpider(scrapy.Spider):
    name = "gmx"

    def start_requests(self):
        urls = [
            'https://www.gmx.ch/magazine/unterhaltung/lifestyle/horoskop/tag/widder',
            'https://www.gmx.ch/magazine/unterhaltung/lifestyle/horoskop/tag/stier',
            'https://www.gmx.ch/magazine/unterhaltung/lifestyle/horoskop/tag/zwilling',
            'https://www.gmx.ch/magazine/unterhaltung/lifestyle/horoskop/tag/krebs',
            'https://www.gmx.ch/magazine/unterhaltung/lifestyle/horoskop/tag/loewe',
            'https://www.gmx.ch/magazine/unterhaltung/lifestyle/horoskop/tag/jungfrau',
            'https://www.gmx.ch/magazine/unterhaltung/lifestyle/horoskop/tag/waage',
            'https://www.gmx.ch/magazine/unterhaltung/lifestyle/horoskop/tag/skorpion',
            'https://www.gmx.ch/magazine/unterhaltung/lifestyle/horoskop/tag/schuetze',
            'https://www.gmx.ch/magazine/unterhaltung/lifestyle/horoskop/tag/steinbock',
            'https://www.gmx.ch/magazine/unterhaltung/lifestyle/horoskop/tag/wassermann',
            'https://www.gmx.ch/magazine/unterhaltung/lifestyle/horoskop/tag/fische'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        sign = response.url.split("/")[-1]
        horoskoptexts = response.css("div.content .page__content>.horoscope::text").extract()
        for horoskoptext in horoskoptexts:
            with open("gmxHoroskops.txt", "a", encoding="utf-8") as horoskopfile:
                horoskopfile.write(sign)
                horoskopfile.write(":")
                horoskopfile.write(horoskoptext)
                horoskopfile.write("\n")
