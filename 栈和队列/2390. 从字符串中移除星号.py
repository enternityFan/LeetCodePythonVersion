# @Time : 2022-09-07 21:56
# @Author : Phalange
# @File : 2390. 从字符串中移除星号.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D


class Solution:
    def removeStars(self, s: str) -> str:
        mystack = []
        for c in s:
            if len(mystack)!=0 and c == "*":
                mystack.pop()
            else:
                mystack.append(c)

        return "".join(mystack)