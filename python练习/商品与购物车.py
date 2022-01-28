# -*- codeing = utf-8 -*-
# @Time : 2022/1/27 14:51
# @AUTHOR : 张志飞
# @File : 商品与购物车.py
# @Software : PyCharm
products=[["iphone",6888],["Macpro",14800],["小米6",2499],["coffee",31],["book",60],["nike",699],["zzfa",1999]]
print("-"*10,"商品列表","-"*10)
i=1
for product in products:
    print(i,product[0],"%d元"%product[1],sep="\t\t")
    i+=1

a=[]

while 1:
    j = input("请输入要购商品序号，一次一个，回车结束（输入 y 表示选完）:")
    if j!="y":
        a.append(int(j))
    else:
        break
a.sort()

print("-"*10,"已购商品列表","-"*10)
i=1
for product in products:
    if i in a:
        print(i,product[0],"%d元"%product[1],sep="\t\t")
    i+=1