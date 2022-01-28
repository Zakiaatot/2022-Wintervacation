# -*- codeing = utf-8 -*-
# @Time : 2022/1/27 20:38
# @AUTHOR : 张志飞
# @File : 函数.py
# @Software : PyCharm
#函数定义
def fx():
    print("-----------------------")
    print("        张宝大傻逼       ")
    print("-----------------------")



def fx1(a,b):
    c=a+b
    print(c)

fx1(1,21)




def fx2(a,b):
    return a+b

print(fx2(1,6))


a=7

def fx3():
    global a      #加了global是对全局变量a进行修改操作
    a=6
    print(a)

fx3()
print(a)
