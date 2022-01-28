# -*- codeing = utf-8 -*-
# @Time : 2022/1/28 8:39
# @AUTHOR : 张志飞
# @File : 写入古诗.py
# @Software : PyCharm
def xgs(a,b) :#把古诗a，写入文件b
    try:
        f=open(b,"w",encoding="utf-8")
        f.write(a)
        print("写入古诗完毕")
    except Exception as result:
        print("写入古诗错误")
        print(result)
    finally:
        f.close()




def cpy(a,b):#把文本a复制到文本b
    try:
        f=open(a,"r",encoding="utf-8")
        c=""
        for gs in f.readlines():
            c=c+gs
        print("复制古诗完毕")
    except Exception as result:
        print("复制古诗错误")
        print(result)
    finally:
        f.close()

    try:
        f=open(b,"w",encoding="utf-8")
        f.write(c)
        print("粘贴古诗完毕")
    except Exception as result:
        print("粘贴古诗错误")
        print(result)
    finally:
        f.close()








'''
xgs("""怒发冲冠，凭栏处、潇潇雨歇。抬望眼、仰天长啸，壮怀激烈。三十功名尘与土，八千里路云和月。莫等闲、白了少年头，空悲切。
靖康耻，犹未雪。臣子恨，何时灭。驾长车，踏破贺兰山缺。壮志饥餐胡虏肉，笑谈渴饮匈奴血。待从头、收拾旧山河，朝天阙。""","gushi.txt")
cpy("gushi.txt","copy.txt")
'''