# -*- codeing = utf-8 -*-
# @Time : 2022/1/28 16:06
# @AUTHOR : 张志飞
# @File : version2.py
# @Software : PyCharm

#此版本目的是实现第一页所有新闻名字和链接的提取,并定期（5秒更新一次）打印到控制台，并尽量用函数实现

#库导入
import urllib.request,urllib.error
import time
from bs4 import BeautifulSoup


#采用c++模式的写法，定义一个主函数
def main():
    while 1:
        loop()




#循环函数，5秒一次
def loop():
    try:
        print("*" * 20)
        print("华大新闻爬虫测试")
        print("*" * 20)

        url = "https://www.hqu.edu.cn/hdxw.htm"
        html = askurl(url)
        bs = BeautifulSoup(html, "html.parser")

        baseurl = "https://www.hqu.edu.cn/"
        for i in range(0,25):  #观察得到第一页的新闻条数为25个，id从0到24
            SJ = bs.find_all('tr', id='line_u15_%d'%i)  # 查找id为line_u15_0的tr标签内容保存至SJ
            x = SJ[0]  # 符合条件的只有一个,所以选第一个

            # 查找输出名字
            y = x.find('font')
            name = y.string
            print(name)

            # 查找输出链接
            y = x.find('a')  # 在tr中查找a标签并存入y
            link = baseurl + y.get('href')  # get提取href内容，最终制作成link
            print(link)
    except Exception as e:
        print("数据处理或打印出错了")
        print(e)
    finally:
        print("*" * 20)
        time.sleep(5)#5秒一次








#用urllib 实现 url访问   并返回html源代码
def askurl(url):
    head={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"} #用户代理，模拟浏览器
    request=urllib.request.Request(url,headers=head) #用head访问
    html=""
    try:
        response=urllib.request.urlopen(request)  #对请求的响应
        html=response.read().decode("utf-8")  #把响应写入html变量
        #print(html)
    except urllib.error.URLError as e:
        print("url访问出错了")
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    #如果有异常，打印错误信息

    return html



main()