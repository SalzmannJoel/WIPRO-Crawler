import scrapy
from scrapy.crawler import CrawlerProcess


class ViversumSpider(scrapy.Spider):
    name = "viversum"

    def start_requests(self):
        urls = [
            'http://www.viversum.ch/tageshoroskop'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        horoskops = response.css("#contentarea>.content-center>.container")
        for horoskop in horoskops:
            sign = horoskop.css(".container>h2::attr(id)").extract_first()
            horoskopcontent = horoskop.css(".container>.imgline::text").extract()
            if sign is not None and horoskopcontent is not None:
                for horoskoptext in horoskopcontent:
                    if self.hasUsefulContent(horoskoptext):
                        with open("viversumHoroskops.txt", "a", encoding="utf-8") as horoskopfile:
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

process.crawl(ViversumSpider)
process.start()
