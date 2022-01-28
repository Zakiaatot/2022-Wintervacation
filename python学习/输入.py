# -*- codeing = utf-8 -*-
# @Time : 2022/1/26 16:23
# @AUTHOR : 张志飞
# @File : 输入.py
# @Software : PyCharm
password=input("请输入密码:")
print("密码是:",password,sep="")
#输入（默认是str类型）

a=10
print(type(a))
#查看数据类型

a=int("123")#强制转换
b=a+100
print(b)
password=int(input("请输入密码:"))