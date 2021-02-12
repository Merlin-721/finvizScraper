# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class finvizScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    Ticker = scrapy.Field()
    Price = scrapy.Field()
    MarketCap = scrapy.Field()
    Dividend = scrapy.Field()
    ROA = scrapy.Field()
    ROE = scrapy.Field()
    ROI = scrapy.Field()
    LTDebtEq = scrapy.Field()
    DebtEq = scrapy.Field()
    GrossM = scrapy.Field()
    OperM = scrapy.Field()
    ProfitM = scrapy.Field()
    # Country = scrapy.Field()
    # Industry = scrapy.Field()
    # PE = scrapy.Field()
    # PEG = scrapy.Field()
    # PS = scrapy.Field()
    # PB = scrapy.Field()
    # FwdPE = scrapy.Field()
    # EPSttm = scrapy.Field()
    # EPSty = scrapy.Field()
    # EPSny = scrapy.Field()
    # EPSp5Y = scrapy.Field()
    # EPSn5Y = scrapy.Field()
    # EPSQQ = scrapy.Field()
    # SalesQQ = scrapy.Field()
    # InsiderOwn = scrapy.Field()
    # InstOwn = scrapy.Field()
    # InsiderTrans = scrapy.Field()
    # InstTrans = scrapy.Field()
    # ShortFloat = scrapy.Field()
    # AnalystRecom = scrapy.Field()
    # TargetPrice = scrapy.Field()
    # AvgVolume= scrapy.Field()
    # Range52W = scrapy.Field()