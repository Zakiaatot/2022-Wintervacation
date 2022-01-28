# -*- codeing = utf-8 -*-
# @Time : 2022/1/26 17:09
# @AUTHOR : 张志飞
# @File : 石头剪刀布.py
# @Software : PyCharm
lx=int(input("请输入：剪刀（0）、石头（1）、布（2）："))
if lx==0:
    print("你出了剪刀")
elif lx==1:
    print("你出了石头")
else:
    print("你出了布")

import random
robot=random.randint(0,2)

if robot==0:
    print("机器人出了剪刀")
elif robot==1:
    print("机器人出了石头")
else:
    print("机器人出了布")

print("结果是：")
if lx==robot:
    print("平局")
elif lx-robot==1 or lx-robot==-2:
    print("你赢了")
else:
    print("你输了")