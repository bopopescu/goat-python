# -*- coding: utf-8 -*-


import scrapy

class ImageItem(scrapy.Item):
    # 保存图片id
    image_id = scrapy.Field()
    # 保存图片下载地址
    download = scrapy.Field()
