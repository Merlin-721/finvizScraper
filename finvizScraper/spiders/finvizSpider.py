import scrapy
from ..items import finvizScraperItem


# debug by going to this:
# C:\Users\merli\anaconda3\envs\TensorflowNN\Lib\site-packages\scrapy\cmdline.py
# set a breakpoint and hit f5



class finvizScraper(scrapy.Spider):
    name = 'finvizScraper'
    start_urls = [
        'https://finviz.com/screener.ashx?v=161&f=cap_small,fa_fpe_profitable,fa_netmargin_pos,sh_instown_u80&ft=2'
    ]

    pageN = 2

    def parse(self, response):
        items = finvizScraperItem() # instantiate class

        Ticker = response.css('.screener-link-primary').css('::text').extract()
        Price = response.css(".screener-body-table-nw:nth-child(16) .screener-link").css('::text').extract()
        MarketCap = response.css(".screener-body-table-nw:nth-child(3) .screener-link").css('::text').extract()
        Dividend= response.css(".screener-body-table-nw:nth-child(4) .screener-link").css('::text').extract()
        ROA = response.css(".screener-body-table-nw:nth-child(5) .screener-link").css('::text').extract()
        ROE = response.css(".screener-body-table-nw:nth-child(6) .screener-link").css('::text').extract()
        ROI = response.css(".screener-body-table-nw:nth-child(7) .screener-link").css('::text').extract()
        LTDebtEq = response.css(".screener-body-table-nw:nth-child(10) .screener-link").css('::text').extract()
        DebtEq = response.css(".screener-body-table-nw:nth-child(11) .screener-link").css('::text').extract()
        GrossM = response.css(".screener-body-table-nw:nth-child(12) .screener-link").css('::text').extract()
        OperM = response.css(".screener-body-table-nw:nth-child(13) .screener-link").css('::text').extract()
        ProfitM = response.css(".screener-body-table-nw:nth-child(14) .screener-link").css('::text').extract()

        items['Ticker'] = Ticker
        items['Price'] = Price
        items['MarketCap'] = MarketCap
        items['Dividend'] = Dividend 
        items['ROA'] = ROA
        items['ROE'] = ROE
        items['ROI'] = ROI
        items['LTDebtEq'] = LTDebtEq
        items['DebtEq'] = DebtEq
        items['GrossM'] = GrossM
        items['OperM'] = OperM
        items['ProfitM'] = ProfitM
        # items['Industry'] = None
        # items['PE'] = None
        # items['PEG'] = None
        # items['PS'] = None
        # items['PB'] = None
        # items['FwdPE'] = None
        # items['EPS (ttm)'] = None
        # items['EPSty'] = None
        # items['EPSny'] = None
        # items['EPSp5Y'] = None
        # items['EPSn5Y'] = None
        # items['EPSQQ'] = None
        # items['SalesQQ'] = None
        # items['InsiderOwn'] = None
        # items['InstOwn'] = None
        # items['InsiderTrans'] = None
        # items['InstTrans'] = None
        # items['ShortFloat'] = None
        # items['AnalystRecom'] = None
        # items['TargetPrice'] = None
        # items['AvgVolum'] = None
        # items['Range52W'] = None

        yield items

        nextPage = 'https://finviz.com/screener.ashx?v=161&f=cap_small,fa_fpe_profitable,fa_netmargin_pos,sh_instown_u80&ft=2&r=' + str(finvizScraper.pageN) + '1'

        if finvizScraper.pageN <= 28:
            yield response.follow(nextPage, callback = self.parse)
            finvizScraper.pageN += 2 