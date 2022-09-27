# @Time : 2022-09-27 12:09
# @Author : Phalange
# @File : 面试题 01.02. 判定是否互为字符重排.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D


class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        mydict = {}
        if len(s1) !=len(s2):
            return False
        for c in s1:
            if c in mydict:
                mydict[c] +=1
            else:
                mydict[c] = 1
        for c in s2:
            if c in mydict and mydict[c] > 0:
                mydict[c] -=1
            else:
                return False
        return True
