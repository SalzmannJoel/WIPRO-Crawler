import scrapy
from scrapy.crawler import CrawlerProcess


class NatuneSpider(scrapy.Spider):
    name = "natune"

    def start_requests(self):
        urls = [
            'https://natune.net/horoskop/tageshoroskop-widder',
            'https://natune.net/horoskop/tageshoroskop-stier',
            'https://natune.net/horoskop/tageshoroskop-zwillinge',
            'https://natune.net/horoskop/tageshoroskop-krebs',
            'https://natune.net/horoskop/tageshoroskop-loewe',
            'https://natune.net/horoskop/tageshoroskop-jungfrau',
            'https://natune.net/horoskop/tageshoroskop-waage',
            'https://natune.net/horoskop/tageshoroskop-skorpion',
            'https://natune.net/horoskop/tageshoroskop-schuetze',
            'https://natune.net/horoskop/tageshoroskop-steinbock',
            'https://natune.net/horoskop/tageshoroskop-wassermann',
            'https://natune.net/horoskop/tageshoroskop-fische'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        sign = (response.url.split("/")[-1]).split("-")[-1]
        horoskoptext = response.css(".szcontent>.szfulldesc>div:nth-child(2)::text").extract_first()
        with open("natuneHoroskops.txt", "a", encoding="utf-8") as horoskopfile:
            horoskopfile.write(sign)
            horoskopfile.write(":")
            horoskopfile.write(horoskoptext)
            horoskopfile.write("\n")

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(NatuneSpider)
process.start()
