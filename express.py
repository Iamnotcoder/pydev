#coding=utf8
# wei.wang what hurts more,the pain of hard work or the pain of regret?
__author__ = 'v'
__date__ = '2017/2/6'

import  urllib2
import  re
print """1:顺丰速运
2:圆通快递
3:中通快递
4:EMS
"""
print "*" * 30
company = {1:"shunfeng", 2:"yuantong", 3:"zhongtong", 4:"EMS"}
ID = int(raw_input( "请选择相应的快递公司编号: "))
ordID = int(raw_input("请输入你的快递单号: "))
# request = urllib2.Request(url=url)
# response = urllib2.urlopen(request)
# content =response.read()
def getHtml(url):
    content = urllib2.urlopen(urllib2.Request(url=url)).read()
    partten = re.compile('{"time":(.*?),.*?"context":(.*?)","location":.*?},', re.S)
    items = re.findall(partten, content)
    for item in items:
        times = item[0].replace('<br />', '\n')
        locations = item[1].replace('<br />', '\n')
        print times, locations
def search():
    url = "http://www.kuaidi100.com/query?type=%s&postid=%s&id=1&valicode"    % (company[ID],ordID)
    getHtml(url)
if __name__ == '__main__':
    print "查询中，请稍等..."
    print "*" * 30
    search()
    print "*" * 30
    print "查询完成，请注意查收您的快递！！！"
    