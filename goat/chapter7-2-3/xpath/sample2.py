from lxml import etree


# 资源文件的读取方式二

# 从html文件中读取数据   这次的输出结果略有不同，多了一个 DOCTYPE 的声明，不过对解析无任何影响
html = etree.parse('./test.html', etree.HTMLParser())
result = etree.tostring(html)
print("文件中读取数据：\n"+result.decode('utf-8'))


