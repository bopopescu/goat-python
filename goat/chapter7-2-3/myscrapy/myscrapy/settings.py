# -*- coding: utf-8 -*-

# Scrapy settings for myscrapy project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'myscrapy'

SPIDER_MODULES = ['myscrapy.spiders']
NEWSPIDER_MODULE = 'myscrapy.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'myscrapy (+http://www.yourdomain.com)'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3493.3 Safari/537.36'

# Obey robots.txt rules  遵守机器人协议
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False
HTTPERROR_ALLOWED_CODES = [403]#上面报的是403，就把403加入。
# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    "charset": "utf-8",
    "Accept-Encoding": "gzip",
    "referer": "https://servicewechat.com/wx9f2867fc22873452/31/page-frame.html",
    # "authorization": settings.authorization,
    "authorization": "",
    "version": "TYC-XCX-WX",
    "content-type": "application/json",
    # "User-Agent": "Mozilla/5.0 (Linux; Android 7.0; MI 5 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.98 Mobile Safari/537.36 MicroMessenger/6.7.3.1360(0x2607033D) NetType/WIFI Language/zh_CN Process/appbrand0",
    "Host": "api9.tianyancha.com",
    "Connection": "Keep-Alive",
    'Accept-Language': 'en',
    # 'user-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
    #  'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3493.3 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Cookie': r'aliyungf_tc=AQAAAApzOmtgAggAFjAuOzR+TTJX4OGF; csrfToken=bK_r_2NJsMXoOJZMCZ2iqCGF; TYCID=b8e65f205dc411eabc3b850f8723860f; undefined=b8e65f205dc411eabc3b850f8723860f; ssuid=920059456; RTYCID=e15ac73f01a04e9da6951816027f336e; CT_TYCID=fb295c1c501649109bcf6474232f5c95; _ga=GA1.2.658118465.1583291014; _gid=GA1.2.311028762.1583291014; bannerFlag=true; tyc-user-phone=%255B%252218604232063%2522%255D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODYwNDIzMjA2MyIsImlhdCI6MTU4MzI5MTQ0NCwiZXhwIjoxNjE0ODI3NDQ0fQ.84WPHUI94sLO4xZNCPJ7yfsuj1JbitbC6RkHpoVnrWYFi-frfUl_8x5vyup_sc1BYIeq49D44afqlTynlQwlkQ; tyc-user-info=%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A0%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522bidSubscribe%2522%253A%2522-1%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522monitorUnreadCount%2522%253A%25220%2522%252C%2522discussCommendCount%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODYwNDIzMjA2MyIsImlhdCI6MTU4MzI5MTQ0NCwiZXhwIjoxNjE0ODI3NDQ0fQ.84WPHUI94sLO4xZNCPJ7yfsuj1JbitbC6RkHpoVnrWYFi-frfUl_8x5vyup_sc1BYIeq49D44afqlTynlQwlkQ%2522%252C%2522claimPoint%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522myAnswerCount%2522%253A%25220%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522signUp%2522%253A%25221%2522%252C%2522nickname%2522%253A%2522%25E5%258C%2585%25E6%258B%25AF%2522%252C%2522privateMessagePointWeb%2522%253A%25220%2522%252C%2522privateMessagePoint%2522%253A%25220%2522%252C%2522isClaim%2522%253A%25220%2522%252C%2522new%2522%253A%25221%2522%252C%2522pleaseAnswerCount%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522mobile%2522%253A%252218604232063%2522%257D; jsid=SEM-BAIDU-PZ2003-SY-000001; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1583291013,1583329032,1583329344; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1583365614; token=7604f030f05446b0859ee50fdff51087; _utm=f2502421747a4211922073e4ba61bb3b; cloud_token=9b21d015cc2644c184faf593c50ff8e0'
}

