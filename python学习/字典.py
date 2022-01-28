# -*- codeing = utf-8 -*-
# @Time : 2022/1/27 15:26
# @AUTHOR : 张志飞
# @File : 字典.py
# @Software : PyCharm
info={"zzf":66,"zb":"散兵"}
print(info["zb"])#字典查找
print(info.get("666"))#get查找
print(info.get("666","没找到"))#未找到


#增
info["zgl"]="66"

#删
del info["zgl"]
print(info)
info.clear()#清空

#改
info["zb"]="dm"



#查
info={"zzf":66,"zb":"散兵"}
print(info.keys()) #得到所有键
print(info.values()) #得到所有的值
print(info.items())#每个键值都是元组

for key,value in info.items():
    print("key=%s,value=%s"%(key,value))
