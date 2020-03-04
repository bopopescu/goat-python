# import urllib
import requests
from bs4 import BeautifulSoup
from urllib import parse
import time
def craw(url,key_word,x,new_num):
    if x == 0:
        re = 'https://www.tianyancha.com/search?key='+key_word
    else:
        re = 'https://www.tianyancha.com/search/p{}?key={}'.format(x-1,key_word)
    headers = {
        'Host': 'www.tianyancha.com',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': r'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Referer': re,#'https://www.tianyancha.com/search?key=%E5%B1%B1%E4%B8%9C%20%E7%A7%91%E6%8A%80',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': r'aliyungf_tc=AQAAAApzOmtgAggAFjAuOzR+TTJX4OGF; csrfToken=bK_r_2NJsMXoOJZMCZ2iqCGF; TYCID=b8e65f205dc411eabc3b850f8723860f; undefined=b8e65f205dc411eabc3b850f8723860f; ssuid=920059456; RTYCID=e15ac73f01a04e9da6951816027f336e; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1583291013; CT_TYCID=fb295c1c501649109bcf6474232f5c95; _ga=GA1.2.658118465.1583291014; _gid=GA1.2.311028762.1583291014; bannerFlag=true; tyc-user-info=%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522bidSubscribe%2522%253A%2522-1%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522monitorUnreadCount%2522%253A%25220%2522%252C%2522discussCommendCount%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODYwNDIzMjA2MyIsImlhdCI6MTU4MzI5MTQ0NCwiZXhwIjoxNjE0ODI3NDQ0fQ.84WPHUI94sLO4xZNCPJ7yfsuj1JbitbC6RkHpoVnrWYFi-frfUl_8x5vyup_sc1BYIeq49D44afqlTynlQwlkQ%2522%252C%2522claimPoint%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522myAnswerCount%2522%253A%25220%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522signUp%2522%253A%25221%2522%252C%2522nickname%2522%253A%2522%25E5%258C%2585%25E6%258B%25AF%2522%252C%2522privateMessagePointWeb%2522%253A%25220%2522%252C%2522privateMessagePoint%2522%253A%25220%2522%252C%2522isClaim%2522%253A%25220%2522%252C%2522new%2522%253A%25221%2522%252C%2522pleaseAnswerCount%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522mobile%2522%253A%252218604232063%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODYwNDIzMjA2MyIsImlhdCI6MTU4MzI5MTQ0NCwiZXhwIjoxNjE0ODI3NDQ0fQ.84WPHUI94sLO4xZNCPJ7yfsuj1JbitbC6RkHpoVnrWYFi-frfUl_8x5vyup_sc1BYIeq49D44afqlTynlQwlkQ; tyc-user-phone=%255B%252218604232063%2522%255D; token=6feb11a42cdb4c348ade3e787679f6a8; _utm=b87f27cd5d8c47a8b3c0efae4879dc1e; cloud_token=4163081dbcef46fb9d52410ddd61ffa5; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1583307297',
    }
    try:
        response = requests.get(url,headers = headers) # import requests
        if response.status_code != 200:
            response.encoding = 'utf-8'
            print(response.status_code)
            print('ERROR')
        soup = BeautifulSoup(response.text,'lxml') # from bs4 import BeautifulSoup
    except Exception:
        print('请求都不让，这天眼查也搞事情吗？？？')
    try:
        com_all_info = soup.body.select('.mt74 .container.-top .container-left .search-block.header-block-container')[0]
        com_all_info_array = com_all_info.select('.search-item.sv-search-company')

    except Exception:
        print('好像被拒绝访问了呢...请稍后再试叭...')
    try:
        for i in range(new_num,len(com_all_info_array)):
            try:
                temp_g_name = com_all_info_array[i].select('.content .header .name')[0].text    #获取公司名
                gaga = parse.quote(temp_g_name)
                re = 'https://www.tianyancha.com/search/p{}?key={}'.format(0,gaga)
                # re = 'https://www.tianyancha.com/search?key=' + temp_g_name
                response = requests.get(re,headers = headers) # import requests
                soup = BeautifulSoup(response.text,'lxml') # from bs4 import BeautifulSoup
                table = soup.table
                tr_arr = table.find_all("tr")
                for tr in tr_arr:
                    tds = tr.find_all('td');
                    print(tds[3].get_text())
            except Exception:
                print(temp_g_name+"-信息不完整，>>>>跳过>>下一个")
    except Exception:
        print("这页有毒，换下一页")


if __name__ == '__main__':
    global g_name_list
    global g_state_list
    global r_name_list
    global g_money_list
    global g_date_list
    global r_phone_list
    global r_email_list
    #    global g_desc_list

    g_name_list=[]
    g_state_list=[]
    r_name_list=[]
    g_money_list=[]
    g_date_list=[]
    r_phone_list=[]
    r_email_list=[]
    #    g_desc_list=[]


    key_word = input('请输入您想搜索的关键词：')
    try:
        new_num = int(input('请输入您想从第几页检索：'))-1
    except Exception:
        new_num = 0
    try:
        num = int(input('请输入您想检索的次数：'))+1
    except Exception:
        num = 6
    try:
        sleep_time = int(input('请输入每次检索延时的秒数：'))
    except Exception:
        sleep_time = 5

    key_word = parse.quote(key_word)
    for x in range(1,num): # 请输入每次检索延时的秒数
        url = r'https://www.tianyancha.com/search/p{}?key={}'.format(x,key_word)
        #        print(r'https://www.tianyancha.com/search/p{}?key={}'.format(x,key_word))
        #        url = r'https://www.tianyancha.com/search/p2?key=%E5%B1%B1%E4%B8%9C%20%E7%A7%91%E6%8A%80'
        s1 = craw(url,key_word,x,new_num)
        print(s1)
        time.sleep(sleep_time)