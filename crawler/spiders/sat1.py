import scrapy
from scrapy.crawler import CrawlerProcess


class SateinsSpider(scrapy.Spider):
    name = "sateins"

    def start_requests(self):
        urls = [
            'https://www.sat1.ch/ratgeber/horoskop/tageshoroskop/widder',
            'https://www.sat1.ch/ratgeber/horoskop/tageshoroskop/stier',
            'https://www.sat1.ch/ratgeber/horoskop/tageshoroskop/zwillinge',
            'https://www.sat1.ch/ratgeber/horoskop/tageshoroskop/krebs',
            'https://www.sat1.ch/ratgeber/horoskop/tageshoroskop/loewe',
            'https://www.sat1.ch/ratgeber/horoskop/tageshoroskop/jungfrau',
            'https://www.sat1.ch/ratgeber/horoskop/tageshoroskop/waage',
            'https://www.sat1.ch/ratgeber/horoskop/tageshoroskop/skorpion',
            'https://www.sat1.ch/ratgeber/horoskop/tageshoroskop/schuetze',
            'https://www.sat1.ch/ratgeber/horoskop/tageshoroskop/steinbock',
            'https://www.sat1.ch/ratgeber/horoskop/tageshoroskop/wassermann',
            'https://www.sat1.ch/ratgeber/horoskop/tageshoroskop/fische'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        sign = response.url.split("/")[-1]
        # alternativeSign = response.css(".content .content-area:nth-child(1) h1::text").extract_first()
        horoskoptexts = response.css(".content .content-area:nth-child(2) .article-page-text p::text").extract()
        for horoskoptext in horoskoptexts:
            with open("sateinsHoroskops.txt", "a", encoding="utf-8") as horoskopfile:
                horoskopfile.write(sign)
                horoskopfile.write(":")
                horoskopfile.write(horoskoptext)
                horoskopfile.write("\n")
