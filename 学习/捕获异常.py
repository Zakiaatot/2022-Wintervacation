# -*- codeing = utf-8 -*-
# @Time : 2022/1/28 8:28
# @AUTHOR : 张志飞
# @File : 捕获异常.py
# @Software : PyCharm
import tarfile

try:
    print(num)
except NameError:
    print("没定义")

try:
    f=open("123.txt","r")
except IOError as result:
    print("没这个文件:",result)


try:
    f=open("123.txt","r")
except Exception as result:#exception承接任何异常
    print(result)



try:
    f=open("123.txt","r")

except Exception as result:
    print(result)

finally:
    f.close()