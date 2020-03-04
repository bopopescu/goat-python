
import requests

from lxml import etree

#获取用来打开url的session
sessions = requests.session()
'''
给sssion设置代理，
因为一般的网站没有这个的话，
会拒绝我们的爬虫访问,
因此我们在这模拟谷歌浏览器访问
'''
sessions.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36'

#进行访问获取源码
r = sessions.get(
    'https://baike.baidu.com/item/%E4%B8%AD%E5%9B%BD%E5%9C%B0%E9%9C%87%E5%B1%80%E9%83%91%E5%B7%9E%E5%9F%BA%E7%A1%80%E5%B7%A5%E7%A8%8B%E5%8B%98%E5%AF%9F%E7%A0%94%E7%A9%B6%E9%99%A2%E6%A1%A9%E5%9F%BA%E6%A3%80%E6%B5%8B%E4%B8%AD%E5%BF%83')
#给怕取下来的数据指定解码格式
r.encoding = 'utf-8'
text = r.text
#将网页源代码进行树结构化，以便于使用xpath
content = etree.HTML(text)
#使用xpath提取标签h1中的内容
h = content.xpath('//h1')
h1 = h[0].xpath('string(.)').strip()
print(h1)

d = content.xpath("//div[@label-module='lemmaSummary']")
d1 = d[0].xpath('string(.)').strip()
print(d1)
