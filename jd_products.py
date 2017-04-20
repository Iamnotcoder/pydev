#coding=utf8
# wei.wang what hurts more,the pain of hard work or the pain of regret?
__author__ = 'v'
__date__ = '2017/3/6'
import requests
from bs4 import BeautifulSoup
page = 2
#url = 'http://audaque.com/'
# page = int(raw_input("请输入要爬取的页面： "))
# for i in range(page):
url = 'http://www.qiushibaike.com/text/page/%s/?s=4968921' % page
headers = {"User-Agent":"Mozilla/5.0"}
try:
    r = requests.get(url=url, headers=headers, timeout=30)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    # print r.text
except:
    print "网页获取失败，请检查您的网络是否连接或者URL地址是否正确"

soup = BeautifulSoup(r.text, 'lxml')
print soup.span
# content = soup.find_all('span', text=None)
# print content
# for items in content:
#     print items.encode('utf8')
# items = content.find_all()
# print soup.prettify()
# print soup.title
# print soup.span