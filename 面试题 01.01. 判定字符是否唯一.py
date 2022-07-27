# @Time : 2022-03-02 18:14
# @Author : Phalange
# @File : 面试题 01.01. 判定字符是否唯一.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D

from typing import *
class Solution:
    def isUnique(self, astr: str) -> bool:
        if len(astr)< 2:
            return True
        astr =  "".join((lambda x: (x.sort(), x)[1])(list(astr)))

        for i in range(len(astr)-1):
            if astr[i] == astr[i+1] :
                return False
        return True



s = Solution
str = "kzwunahkiz"
s.isUnique(s,str)