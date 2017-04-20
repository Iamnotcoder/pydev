#coding=utf8
# wei.wang what hurts more,the pain of hard work or the pain of regret?
__author__ = 'v'
__date__ = '2017/3/16'
from datetime import datetime,date
import datetime
import  time
import requests
import json

#2017-03-29
#2017-04-05

def main():
    class_dir = {'A':"08:30-17:30", 'B':"15:30-23:30", 'C':"23:30-08:30"}
    date_list = []
    print ("班次如下，请输入初始班次>: A|B|C")
    print ("""A:08:30-17:30
B:15:30-23:30
C:23:30-08:30""")

    # a = input('请输入起始日期，格式为yyyy-m-d')
    a = '2017-03-01'
    # b = input('请输入终止日期，格式为yyyy,m,d')
    b = '2017-03-20'
    t = time.strptime(a, "%Y-%m-%d")
    p = time.strptime(b, "%Y-%m-%d")
    y,m,d = t[0:3]
    y1,m1,d1 = p[0:3]
    begin = date(y,m,d)
    end =  date(y1,m1,d1)
    d = begin
    delta = datetime.timedelta(days=1)
    while d <= end:
        date_list.append(d.strftime("%Y%m%d"))
        d += delta


    worktime_list = []
    for i in date_list:
        url = "http://www.easybots.cn/api/holiday.php?d=" + i
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        worktime = (r.json())
        if worktime[i] == '0':
        # {0：工作日， 1：周末， 2：法定节假日}
            worktime_list.append(i)





if __name__ == '__main__':
    main()

