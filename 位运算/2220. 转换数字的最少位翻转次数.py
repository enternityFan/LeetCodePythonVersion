# @Time : 2022-08-01 20:28
# @Author : Phalange
# @File : 2220. 转换数字的最少位翻转次数.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D


class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        n = start ^ goal # 得到二者不同位的数目
        count = 0
        while n !=0:
            rightOne = n&(~n + 1) #取n最右边的1
            count +=1
            n ^=rightOne # 这里必须用异或，而不能减号，因为如果n是负数的话减号就报错了

        return count
