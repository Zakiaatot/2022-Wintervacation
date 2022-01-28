# -*- codeing = utf-8 -*-
# @Time : 2022/1/28 9:32
# @AUTHOR : 张志飞
# @File : 豆瓣爬虫.py
# @Software : PyCharm
'''
def main():
    print("hello")

if __name__ =="__main__":      #当程序执行时
    main()      #调用函数
'''



from python练习 import 写入古诗 #引用其它文件里的函数,被导入的文件 写入古诗.py 也会被执行一次
写入古诗.xgs("""怒发冲冠，凭栏处、潇潇雨歇。抬望眼、仰天长啸，壮怀激烈。三十功名尘与土，八千里路云和月。莫等闲、白了少年头，空悲切。
靖康耻，犹未雪。臣子恨，何时灭。驾长车，踏破贺兰山缺。壮志饥餐胡虏肉，笑谈渴饮匈奴血。待从头、收拾旧山河，朝天阙。""","gushi.txt")
写入古诗.cpy("gushi.txt","copy.txt")




#豆瓣top250
from bs4 import BeautifulSoup    #网页解析，获取数据
import re    #正则表达式，进行文字匹配
import urllib.request,urllib.error #制定url，获取网页数据
import xlwt #进行excel操作
import sqlite3 #进行sqlite数据库操作

def main():
    baseurl="https://movie.douban.com/top250?start="

    #1.爬取网页
    #2.解析数据
    datalist=getdata(baseurl)


    #3.保存数据
    savepath=".\\豆瓣电影top250.xls"
    savedata(savepath)


#两个主函数
def getdata(baseurl):  #爬取函数
    datalist=[]
    for i in range(0,10):
        url=baseurl+"%d"%(i*25)  #因为豆瓣一页25个电影，共9页
        html=askurl(url)

        #对获取的每一页进行数据解析，beautifulsoup




    return datalist


def savedata(savepath): #保存函数
    print("saved.....")

#爬取副函数,得到html源代码
def askurl(url):
    head={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"} #用户代理，模拟浏览器
    request=urllib.request.Request(url,headers=head) #用head访问
    html=""
    try:
        response=urllib.request.urlopen(request)  #对请求的响应
        html=response.read().decode("utf-8")  #把响应写入html变量
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    #如果有异常，打印错误信息

    return html

# 测试用  askurl("https://boileddog.top")
