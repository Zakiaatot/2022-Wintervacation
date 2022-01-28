# -*- codeing = utf-8 -*-
# @Time : 2022/1/27 21:19
# @AUTHOR : 张志飞
# @File : 文件操作（test.txt）.py
# @Software : PyCharm
f=open("test.txt","w") #open(文件,模式) w为写模式，文件不存在则会自动创建
f.write("fuckyou,zb") #write为写入
f.close()


f=open("test.txt","r")
print(f.read(5))#从指针头开始读5个字符
print(f.read(5))#从指针位置继续读5个
f.close()



f=open("test.txt","r")
print(f.readlines())#以列表方式读取
f.close()



f=open("test.txt","r")
for i in f.readlines():  #输出文本内容
    print(i)
f.close()


f=open("test.txt","r")
print(f.readline())#读取第一行

f.close()

