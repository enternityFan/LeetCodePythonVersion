# @Time : 2022-08-11 17:57
# @Author : Phalange
# @File : 位运算加速效果小例子.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import time
if __name__ == "__main__":
    a = 1
    实验次数= 1e7 # 实验1e10次
    开始时间 = time.time()
    while a <=实验次数:
        a +=1

    结束时间 = time.time()
    print("实验次数:{:},一共耗时:{:}".format(实验次数,结束时间 - 开始时间))
    print("===========================================================")
    print("位运算实验开始===============================================")
    a = 1
    开始时间 = time.time()
    while a <=实验次数:
        a = (a^1) + ((a&1) << 1)
 
    结束时间 = time.time()
    print("实验次数:{:},一共耗时:{:}".format(实验次数,结束时间 - 开始时间))