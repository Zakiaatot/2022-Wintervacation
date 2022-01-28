# -*- codeing = utf-8 -*-
# @Time : 2022/1/27 10:09
# @AUTHOR : 张志飞
# @File : 列表.py
# @Software : PyCharm
list=[1,2,"sadsa","ad"]

print(list[0:3])


'''
#增 3种
print("增加前：")
for i in list:
    print(i)


sr=input("请输入：")
list.append(sr)
#如果sr为列表，会出现列表的嵌套如[1,2,[3,4]],所以两个列表合为一个用extend

b=[1,6,9]
list.extend(b)
#extend

c=[15,17]
list.insert(0,c) #第一个是下标，第二个是数据





print("增加后：")
for i in list:
    print(i)
'''





'''
#删 3种
print("删除前：")
for i in list:
    print(i)

del list[1]

list.pop() #只弹出最后一个

list.remove("ad")#删除指定内容，有多个相同数据时只删除最后一个


print("删除后：")
for i in list:
    print(i)
'''


'''
#改
print("修改前：")
for i in list:
    print(i)

list[0]="966"#直接替换

print("修改后：")
for i in list:
    print(i)
'''

'''
#查
findname=input("输入要查找的数据：")
if findname or int(findname) in list:
    print("yes")
else:
    print("no")
'''
'''
#查2
print(list.index(1,0,4)) #index(待查找数据,起始位置,末位置) index函数返回查找到的下标 区间[0,4)  默认找不到会报错
print(list.count("ad")) #统计有几个ad
'''

'''
#排序和反转
A=[1,4,2,3]
print(A)
A.reverse() #将列表反转
print(A)
A.sort() #升序排列
print(A)
A.sort(reverse=True)#降序
print(A)
'''


#嵌套 即2维数组
B=[["北京大学","清华大学"],["南开大学","天津大学"],["山东大学","中国海洋大学"]]
print(B[0])
print(B[0][0])



#补充 添加序号输出列表
mylist=["a","b","c","d"]

for i,x in enumerate(mylist):
    print(i,x)