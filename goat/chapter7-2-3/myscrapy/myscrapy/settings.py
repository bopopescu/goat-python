# -*- coding: utf-8 -*-

BOT_NAME = 'myscrapy'

SPIDER_MODULES = ['myscrapy.spiders']
NEWSPIDER_MODULE = 'myscrapy.spiders'


# Obey robots.txt rules  遵守机器人协议
ROBOTSTXT_OBEY = False


# 以下报错 由于没加请求头的原因   没有请求头，被网站识别为爬虫程序（所以要模拟浏览器访问）
# Ignoring response <503 https://www.xicidaili.com/nn/>: HTTP status code is not handled or not allowed

DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'user-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
}