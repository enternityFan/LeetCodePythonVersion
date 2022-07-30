# @Time : 2022-07-29 11:39
# @Author : Phalange
# @File : 2351. 第一个出现两次的字母.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        mydict = {}

        for c in s:
            if c in mydict:#出现了两次
                return c
            else:
                mydict[c] =1