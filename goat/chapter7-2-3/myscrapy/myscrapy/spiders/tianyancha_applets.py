# -*- coding: utf-8 -*-
import scrapy


class TianyanchaAppletsSpider(scrapy.Spider):
    name = 'tianyancha_applets'
    allowed_domains = ['tianyancha.com']
    # search_url = ['http://tianyancha.com/']
    search_url = 'https://api9.tianyancha.com/services/v3/search/sNorV4/{}?sortType=0&pageSize=30&pageNum=1'

    def start_requests(self):
        keyword = '深圳市国富黄金股份有限公司'
        yield scrapy.Request(url=self.search_url.format(keyword), meta={'keyword': keyword},)

    def parse(self, response):
        """
        搜索结果解析
        :param response: 搜索响应
        """
        print("*"*40)
        keyword = response.meta.get('keyword')
        print("*"*40)
        # 解析结果
        results = json.loads(response.text)
        companyList = results.get('data').get('companyList')

        if not companyList:
            companyList = [{'name': keyword,'id': '',}]

        for data in companyList:
            name = data.get('name', '').replace('<em>', '').replace('</em>', '').strip()  # 企业名称
            uuid = data.get('id')  # 企业唯一id