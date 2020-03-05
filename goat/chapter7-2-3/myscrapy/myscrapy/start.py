# -*- coding: utf-8 -*-

# 导入 scrapy 框架中用于执行 命令行的工具类
from scrapy import cmdline

# cmdline.execute("scrapy crawl qsbkSpider".split())
# cmdline.execute("scrapy crawl tianyancha_applets".split())
# cmdline.execute("scrapy crawl app01".split())
cmdline.execute("scrapy crawl app02".split())

