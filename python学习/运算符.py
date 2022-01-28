# -*- codeing = utf-8 -*-
# @Time : 2022/1/26 16:33
# @AUTHOR : 张志飞
# @File : 运算符.py
# @Software : PyCharm
'''
if 1:
    1
elif 2:
    2
else:
    3
'''
if True:
    print("TRUE")
    print("ssss")#缩进必须和上面一行相同
else:
    print("false")


score=100
if score>=90 and score<=100:
    print("GOOD!")
elif score>=60 :
    print("Keep going on!")
else :
    print("666!")

#引入库 import
import random
x=random.randint(0,2) #随机生成0到2 3个数字
print(x)
