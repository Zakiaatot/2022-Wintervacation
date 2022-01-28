# -*- codeing = utf-8 -*-
# @Time : 2022/1/26 19:07
# @AUTHOR : 张志飞
# @File : 打印99乘法表.py
# @Software : PyCharm
for i in range(1,10):
    for j in range(1,i+1):
        print("%d*%d=%d"%(i,j,i*j),end="\t")
    print("\n")
#for循环

i=1
while i<10:
    j=1
    while j<=i:
        print("%d*%d=%d" % (i, j, i * j), end="\t")
        j+=1
    print("\n")
    i+=1
#while循环

