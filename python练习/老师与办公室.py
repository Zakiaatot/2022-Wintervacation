# -*- codeing = utf-8 -*-
# @Time : 2022/1/27 14:32
# @AUTHOR : 张志飞
# @File : 老师与办公室.py
# @Software : PyCharm
import random
office=[[],[],[]]
names=["a","b","c","d","e","f","g"]
for i in names:
    j=random.randint(0,2)
    office[j].extend(i)
m=1
for i in office:
    n=len(i)
    print("办公室%d有%d人，分别是："%(m,n),end="\t")
    for j in i:
        print(j,end="\t")
    m+=1
    print("")