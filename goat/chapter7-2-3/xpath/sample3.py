

from lxml import etree

# 向下查找 子节点

html = etree.parse('./test.html', etree.HTMLParser())

# 这里使用 //* 代表匹配所有节点，也就是整个 HTML 文本中的所有节点都会被获取。
result = html.xpath('//*')
print('【//*】  xpath解析结果 %s \n数组长度为 %s' %(result,len(result)))

# 这里要选取所有 li 节点，也就是整个 HTML 文本中的所有 li 节点都会被获取。
result = html.xpath('//li')
print('【//li】 xpath解析结果 %s \n数组长度为 %s' %(result,len(result)))

'''
即选择了所有 li 节点的所有直接 a 子节点。因为// li 用于选中所有 li 节点，/a
用于选中 li 节点的所有直接子节点 a , 二者组合在一起即获取所有 li 节点的所有直接 a 子节点 。
'''
result = html.xpath('//li/a')
print('【//li/a】 xpath解析结果 %s \n数组长度为 %s' %(result,len(result)))


# 获取 ul 节点下的所有子孙 a 节点
result = html.xpath('//ul//a')
print('【//ul/a】 xpath解析结果 %s \n数组长度为 %s' %(result,len(result)))

'''
result = html.xpath('//ul/a')
但是如果这里用//ul/a，就无法获取任何结果了 。 因为/用于获取直接子节点，而在 ul 节点下没有直接的 a 子节点
只有 li 节点，所以无法获取任何匹配结果
'''
# sos 这里我们要注意／和／／的区别，其中／用于获取直接子节点，／／用于获取子孙节点


