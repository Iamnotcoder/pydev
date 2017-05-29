#coding=utf8
# wei.wang what hurts more,the pain of hard work or the pain of regret?
__author__ = 'v'
__date__ = '2017/5/16'
import requests
import down_bean_51cto


host = 'http://u.ifeige.cn/api/'
path = "group_sendmsg"
url = host + path + '?'
data = {
    'secret':'762b7403483c8c324119a4ea65c3a7e5',
    'token':'9ca138a18293d20b6ff18dc67e925472',
    'title':'51CTO 领豆通知',
    'content':down_bean_51cto.get_download_bean(),
    'remark':'已成功领取'
}

# error_code ={
#    200:"成功",
#    10001:"缺少secret或token",
#    10002:"缺少消息标题或内容",
#    10003:"消息模板KEY错误",
#    10004:"secret或token错误",
#    10005:"余额不足"
# }
try:
    r = requests.post(url=url,data=data)
    res = r.json()
    if res['code'] == 200:
        print("信息发送成功")
except:
    print("连接失败")



