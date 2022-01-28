# -*- codeing = utf-8 -*-
# @Time : 2022/1/28 15:02
# @AUTHOR : 张志飞
# @File : version1.py
# @Software : PyCharm

#访问url函数
import urllib.request,urllib.error
def askurl(url):
    head={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"} #用户代理，模拟浏览器
    request=urllib.request.Request(url,headers=head) #用head访问
    html=""
    try:
        response=urllib.request.urlopen(request)  #对请求的响应
        html=response.read().decode("utf-8")  #把响应写入html变量
        #print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    #如果有异常，打印错误信息

    return html


from bs4 import BeautifulSoup
url="https://www.hqu.edu.cn/hdxw.htm"
html=askurl(url)
bs=BeautifulSoup(html,"html.parser")




#只对第一条新闻爬取，打印名字和链接
baseurl="https://www.hqu.edu.cn/"

SJ=bs.find_all('tr',id = 'line_u15_0')#查找id为line_u15_0的tr标签内容保存至SJ
x=SJ[0]#符合条件的只有一个,所以选第一个

#查找输出链接
y=x.find('a')   #在tr中查找a标签并存入y
link=baseurl+y.get('href')#get提取href内容，最终制作成link
print(link)