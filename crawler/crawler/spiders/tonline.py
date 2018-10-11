import scrapy
from scrapy.crawler import CrawlerProcess


class TonlineSpider(scrapy.Spider):
    name = "tonline"

    def start_requests(self):
        urls = [
            'http://horoskop.t-online.de/tageshoroskop/widder',
            'http://horoskop.t-online.de/tageshoroskop/stier',
            'http://horoskop.t-online.de/tageshoroskop/zwilling',
            'http://horoskop.t-online.de/tageshoroskop/krebs',
            'http://horoskop.t-online.de/tageshoroskop/loewe',
            'http://horoskop.t-online.de/tageshoroskop/jungfrau',
            'http://horoskop.t-online.de/tageshoroskop/waage',
            'http://horoskop.t-online.de/tageshoroskop/skorpion',
            'http://horoskop.t-online.de/tageshoroskop/schuetze',
            'http://horoskop.t-online.de/tageshoroskop/steinbock',
            'http://horoskop.t-online.de/tageshoroskop/wassermann',
            'http://horoskop.t-online.de/tageshoroskop/fische'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        sign = response.url.split("/")[-1]
        horoskopcontent = response.css("div#Tcontboxi div.Tart>div>p:first-of-type::text").extract()
        if sign is not None and horoskopcontent is not None:
            for horoskoptext in horoskopcontent:
                if self.hasUsefulContent(horoskoptext):
                    with open("tonlineHoroskops.txt", "a", encoding="utf-8") as horoskopfile:
                        horoskopfile.write(sign)
                        horoskopfile.write(":")
                        horoskopfile.write(horoskoptext.lstrip().rstrip())
                        horoskopfile.write("\n")

    def hasUsefulContent(self, string):
        response = True
        checkstring = string.split()
        if not checkstring:
            response = False
        return response

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(TonlineSpider)
process.start()
