# -*- coding: utf-8 -*-
import scrapy


class App03Spider(scrapy.Spider):
    name = 'app03'
    start_urls = ['http://lab.scrapyd.cn/']

    def parse(self, response):
        # 提取首页所有名言列表，保存至变量mingyan
        result_list = response.css('div.quote')
        mingyan = result_list[0]
        print(mingyan)
        text = mingyan.css('.text::text').extract_first()  # 提取名言
        autor = mingyan.css('.author::text').extract_first()  # 提取作者
        tags = mingyan.css('.tags .tag::text').extract()  # 提取标签
        tags = ','.join(tags)  # 数组转换为字符串
        print("名言：" + text)
        print("作者：" + autor)
        print("标签：" + tags)


