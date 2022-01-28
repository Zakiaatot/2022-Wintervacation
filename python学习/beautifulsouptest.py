# -*- codeing = utf-8 -*-
# @Time : 2022/1/28 11:49
# @AUTHOR : 张志飞
# @File : beautifulsouptest.py
# @Software : PyCharm
import re

from bs4 import BeautifulSoup

file=open(".//zzf.html","r",encoding="utf-8")
html=file.read()
bs=BeautifulSoup(html,"html.parser") #把html语法分割为树型结构
# print(bs.a) 把a标签打印出来，默认只打印第一个 <a href="#">来日方长</a>
#print(bs.title) <title>来日方长 - 学习技术 从这里开始</title>
#print(bs.title.string) 来日方长 - 学习技术 从这里开始  得到文字内容
#print(bs.a.attrs) {'href': '#'} 快速拿到一个标签里的所有属性
#print(bs) 等价于print(html) 但bs的类型为bs4.beautifulsoup


#遍历
#print(bs.head.contents)
#print(bs.head.contents[1]) <meta content="upgrade-insecure-requests" http-equiv="Content-Security-Policy"/>



#搜索
#find_all()
#字符串过滤：会查找字符串完全匹配的内容
t_list=bs.find_all("a")#查找标签完全是a的内容
#print(t_list)

#正则表达式搜索：search()
import re
t_list=bs.find_all(re.compile("a"))#查找标签包含a的内容
#print(t_list)


#方法 ：传入一个函数（方法），根据函数的要求来搜索

#2.kwargs 参数搜索
t_list=bs.find_all(class_=True)
for i in t_list:
   pass


#3.text参数
t_list=bs.find_all(text="飞哥") #完全符合条件会被记录
for i in t_list:
    pass

import re
t_list=bs.find_all(text=re.compile("飞"))#包含飞的会被记录
for i in t_list:
    pass

#limit
t_list=bs.find_all("a",limit=3)#只找到前三个
for i in t_list:
    pass



#css选择器
#print(bs.select('title')) [<title>来日方长 - 学习技术 从这里开始</title>]
#通过类名和标签和id来查找
