#coding=utf8
# wei.wang what hurts more,the pain of hard work or the pain of regret?
#pip install moudle_name --trusted-host mirrors.aliyun.com
__author__ = 'v'
__date__ = '2017/4/3'
import requests
import xlwt
import time
from bs4 import BeautifulSoup as BS

print("请耐心等候，页面爬取中。。。。。。")
# time.sleep(3)

def getHtml(city, kw1, pages):
    result = []
    for i in range(1, pages):
        headers = {"User-Agent":"Mozilla/5.0"}
        url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%s&kw=%s&p=%d&kt=3&isadv=0' % (city, kw1, i)
        # url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=深圳&kw=运维&p=1&kt=3&isadv=0'
        print(url)
        try:
            r = requests.get(url=url,headers=headers)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
        except:
            print("网页获取失败，请检查您的网络是否连接或者URL地址是否正确")
        soup = BS(r.text, 'lxml')

        companys = soup.select("table.newlist > tr > td.gsmc")
        job_name = soup.select("table.newlist > tr > td.zwmc > div > a")
        salarys = soup.select("table.newlist > tr > td.zwyx")
        locations = soup.select("table.newlist > tr > td.gzdd")
        times = soup.select("table.newlist > tr > td.gxsj > span")
        #62

        for company, name, salary, location, time in zip(companys, job_name, salarys, locations, times):

            data = [
                company.get_text(),
                name.get_text(),
                salary.get_text(),
                location.get_text(),
                time.get_text()
            ]

            result.append(data)
    return result
    # print(len(result))
    # print(result)



def writeExcel(headers, v):
    v = getHtml(city, kw1, pages)
    wb = xlwt.Workbook()
    sh = wb.add_sheet('job-informations', cell_overwrite_ok=True)

    for i in range(len(v)):
        for j in range(len(headers)):
            sh.write(0,j,headers[j])
            sh.write(i,j,v[i][j])
    # 保存文件
    wb.save('jobs.xls')

# print("*" * 20)
# print('页面打印完毕。。。。。。')

if __name__ == '__main__':
    city = input('请输城市名称> ')
    kw1 = input("请输入工作关键字关键字> ")
    pages = int(input("请输入需要爬取的页数> "))
    getHtml(city, kw1, pages)
    headers = ['公司', '岗位', '薪资', '地点', '发布时间']
    writeExcel(headers, getHtml(city, kw1, pages))
