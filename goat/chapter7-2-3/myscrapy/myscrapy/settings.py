# -*- coding: utf-8 -*-

BOT_NAME = 'myscrapy'

SPIDER_MODULES = ['myscrapy.spiders']
NEWSPIDER_MODULE = 'myscrapy.spiders'


# Obey robots.txt rules  遵守机器人协议
ROBOTSTXT_OBEY = False


# 以下报错 由于没加请求头的原因   没有请求头，被网站识别为爬虫程序（所以要模拟浏览器访问）
# Ignoring response <503 https://www.xicidaili.com/nn/>: HTTP status code is not handled or not allowed


# 一般请求头
# DEFAULT_REQUEST_HEADERS = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#     'Accept-Language': 'en',
#     'user-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
# }


# 天眼查  请求头
DEFAULT_REQUEST_HEADERS = {
    'Host': 'www.tianyancha.com',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': r'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': r'TYCID=b8e65f205dc411eabc3b850f8723860f; undefined=b8e65f205dc411eabc3b850f8723860f; ssuid=920059456; RTYCID=e15ac73f01a04e9da6951816027f336e; CT_TYCID=fb295c1c501649109bcf6474232f5c95; _ga=GA1.2.658118465.1583291014; _gid=GA1.2.311028762.1583291014; tyc-user-phone=%255B%252218604232063%2522%255D; jsid=SEM-BAIDU-PZ2003-SY-000001; aliyungf_tc=AQAAAEWRCWZ3pwgAFjAuO7CZlPBaWs9N; csrfToken=3qtyVhy_t5yln8pGfiMO_LR7; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1583329032,1583329344,1583399100,1583399112; tyc-user-info=%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522myAnswerCount%2522%253A%25220%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522privateMessagePointWeb%2522%253A%25220%2522%252C%2522nickname%2522%253A%2522%25E5%258C%2585%25E6%258B%25AF%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522privateMessagePoint%2522%253A%25220%2522%252C%2522state%2522%253A%25220%2522%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522isClaim%2522%253A%25220%2522%252C%2522bidSubscribe%2522%253A%2522-1%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522discussCommendCount%2522%253A%25220%2522%252C%2522monitorUnreadCount%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522claimPoint%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODYwNDIzMjA2MyIsImlhdCI6MTU4MzM5OTg3NSwiZXhwIjoxNjE0OTM1ODc1fQ.-WUFs9rJEagy_V7i1FAJgMGcikepddAQGFQjLevoIfz2pupJNrfRny30SOqAcONyk7fQQTwIBGIiYtOeu9WwIw%2522%252C%2522pleaseAnswerCount%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252218604232063%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODYwNDIzMjA2MyIsImlhdCI6MTU4MzM5OTg3NSwiZXhwIjoxNjE0OTM1ODc1fQ.-WUFs9rJEagy_V7i1FAJgMGcikepddAQGFQjLevoIfz2pupJNrfRny30SOqAcONyk7fQQTwIBGIiYtOeu9WwIw; bannerFlag=true; token=2bebfe3934bf43fd93e6646642bb9089; _utm=723dc887af2b430bb0589fe9df0a1b24; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1583401998',
}