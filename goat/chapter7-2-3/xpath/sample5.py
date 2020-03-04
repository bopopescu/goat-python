from lxml import etree


# 文本获取

# text（）前面是／，而此处／的含义是选取直接子节点，很明显 l i 的直接子节点都是 a 节点
html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li[@class="item-0"]/text()')
print(result)

# 获取 属性为item-0的所有li节点  下的直接子节点a 下的所有文本内容
result = html.xpath('//li[@class="item-0"]/a/text()')
print(result)