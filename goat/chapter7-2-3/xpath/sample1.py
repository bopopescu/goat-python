
# 这里首先导人 lxml 库的 etree 模块
from lxml import etree

text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''

'''
调用 HTML 类进行初始化，这
样就成功构造了一个 XPath 解析对象。 这里需要注意的是， HTML 文本中的最后一个 li 节点是没有
闭合的，但是 etree 模块可以自动修正 HTML 文本
'''
html = etree.HTML(text)
# 这里我们调用 tostring 方法即可输出修正后的 HTML 代码，但是结果是 bytes 类型
result = etree.tostring(html)
# 这里利用 decode 方法将其转成 str 类型
print(result.decode('utf-8'))
