#coding=utf8
# wei.wang what hurts more,the pain of hard work or the pain of regret?
__author__ = 'v'
__date__ = '2017/4/19'
import requests

with open('raw_cookies.txt') as f:
    cookies = {}
    for line in f.read().split(';'):
        key, val = line.strip().split('=', 1)
        cookies[key] = val
    # print(cookies)
s = requests.Session()
url = 'https://www.zhihu.com/#signin'
headers = {"User-Agent":"Mozilla/5.0"}
r = s.get(url=url,headers=headers,cookies=cookies, verify=False)
# print(s.get(url=url))
print(r.text)