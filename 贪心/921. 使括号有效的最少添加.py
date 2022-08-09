# @Time : 2022-08-09 17:57
# @Author : Phalange
# @File : 921. 使括号有效的最少添加.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import collections


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        mystack = []
        for c in s:
            if c == "(":
                mystack.append(c)
            elif c == ")" :
                if mystack != [] and mystack[-1] == "(":
                    mystack.pop()
                else:
                    mystack.append(c)
        return len(mystack)


print(Solution().minAddToMakeValid("()))"))