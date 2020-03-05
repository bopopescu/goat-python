

# 缺少模块报错：

    开始菜单选择运行，输入cmd运行，然后cd命令进入到python安装目录下的Scripts文件中，
        C:\Program Files (x86)\Python36-32\Scripts 
    安装好Python后，在cmd中输入以下命令   pip install scrapy 
    
    如果使用上面的命令太慢。国内可以使用豆瓣源进行加速。  也有阿里云加速
    pip install -i  https://pypi.douban.com/simple scrapy 
    pip install scrapy -i  http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com 
    pip install pypiwin32 -i  http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com 
    pip install beautifulsoup4 -i  http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com 
    pip install jsonpath -i  http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com 
    pip install pymongo -i  http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com 
    安装完成之后在命令行输入  scrapy -v  验证是否安装成功


     切换目录到    E:\Code\Python\MyPython\goat-python\goat\chapter7-2-3
     输入命令：  scrapy startproject [项目名]，会在当前目录创建一个Scrapy 项目
     scrapy startproject myscrapy
     
     命令行出现这样的结果说明创建成功！
     You can start your first spider with:
         cd myscrapy
         scrapy genspider example example.com
       
         
         
     下面生成一个模板   以管理员方式 打开cmd 命令行
     切换到目录   E:\Code\Python\MyPython\goat-python\goat\chapter7-2-3\myscrapy 
     Terminal中 输入 scrapy genspider BaiduSpider http://www.baidu.com
                     scrapy genspider qsbkSpider "qiushibaike.com"
                     scrapy genspider tianyancha_applets "tianyancha.com"
                     scrapy genspider app01  "lab.scrapyd.cn"
                     scrapy genspider app02  "lab.scrapyd.cn"
     运行成功后 再 myscrapy/spiders/ 目录下 会多出一个 BaiduSpider.py 模板文件
     
     这说明我们的spider创建成功。可以在pytharm中使用这个 强大的框架了。
     
    
# 项目结构
    ├── quotes
    
    │   ├── __init__.py
    
    │   ├── items.py       存放 model，做持久化时使用的
    
    │   ├── middlewares.py  中间件  下载器中间件(加入代理或请求头)、爬虫中间件(过滤掉无用数据)
    
    │   ├── pipelines.py   做持久化时使用的
    
    │   ├── settings.py   所有和下载属性相关的内容都在这里设置  延时请求、加请求头等等
    
    │   └── spiders   自己写的爬虫文件目录
    
    └── scrapy.cfg      整个项目的配置文件


# settings.py 
    # Obey robots.txt rules  遵守机器人协议 改成 False
    ROBOTSTXT_OBEY = False
    
    
    DEFAULT_REQUEST_HEADERS 打开 并增加 请求头
    'user-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
    
# 运行    
    切换目录： E:\Code\Python\MyPython\goat-python\goat\chapter7-2-3\myscrapy
    命令行中输入： scrapy crawl 【启动类名】
    scrapy crawl qsbkSpider
    
    
    
    由于每次都在命令行操作 过于麻烦 新建 start.py 
    使用scrapy 提供的命令行工具来简化开发与调试
    cmdline.execute("scrapy crawl qsbkSpider".split())
    就可以打断点进行调试了！！！