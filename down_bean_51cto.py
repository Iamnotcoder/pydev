#coding=utf8
# wei.wang what hurts more,the pain of hard work or the pain of regret?
__author__ = 'v'
__date__ = '2017/5/28'
import requests
import load_cookies
# import feixin_messages

headers = {"User-Agent":"Mozilla/5.0"}

# def load_51():
#     url = 'http://home.51cto.com/index?reback=http://down.51cto.com'
#     try:
#         s = requests.Session()
#         r = s.get(url=url,headers=headers,cookies=load_cookies.load_cookies('cookie_51cto.txt'), verify=False)
#         r.raise_for_status()
#         r.encoding = r.apparent_encoding
#         print(r.text)
        # print("登录成功")
    # except:
    #     print("网页获取失败，请检查您的网络是否连接或者URL地址是否正确")

def get_download_bean():
    url = "http://down.51cto.com/download.php?do=getfreecredits"
    try:
        s = requests.Session()
        r = s.get(url=url,headers=headers,cookies=load_cookies.load_cookies('cookie_51cto.txt'), verify=False)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        # print(r.text)
        data = r.text.split(',')
        # print(data)
        msg = ''
        # print("登录成功")
        # 邮件信息
        if data[0] == "0":
            print("下载豆领取失败！！！")
            msg += "下载豆领取失败！！！"
        elif data[0] == "1":
            print("今天已领取！！！已领取" + data[1] + "个下载豆！！！")
            msg += "今天已领取！！！已领取" + data[1] + "个下载豆！！！"
        else:
            print("成功领取" + data[1] +"个下载豆，目前拥有" + data[0] + "个下载豆！")
            msg += "成功领取" + data[1] +"个下载豆，目前拥有" + data[0] + "个下载豆！"
        return msg
    except:
        print("下载失败，请检查您的网络是否连接或者URL地址是否正确")





# if __name__ == '__main__':
#     load_51()
    # get_download_bean()
