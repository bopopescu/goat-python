

from lxml import etree

# 向上查找 父节点

html = etree.parse('./test.html', etree.HTMLParser())

# 现在首先选中 href 属性为 link4.html 的 a 节点，然后再获取其父节点，然后再获取其 class属性
result = html.xpath('//a[@href="link4.html"]/../@class')
print('【////a[@href="link4.html"]/../@class】  xpath解析结果 %s \n数组长度为 %s' %(result,len(result)))

# 在选取的时候，我们还可以用@符号进行属性过滤 。 比如，这里如果要选取 class 为 item-1 的 li节点
result = html.xpath('//li[@class="item-0"]')
print('【//li[@class="item-0"]】  xpath解析结果 %s \n数组长度为 %s' %(result,len(result)))