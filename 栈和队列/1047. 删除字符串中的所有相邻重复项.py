# @Time : 2022-09-07 21:29
# @Author : Phalange
# @File : 1047. 删除字符串中的所有相邻重复项.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D


class Solution:
    def removeDuplicates(self, s: str) -> str:
        mystack = []
        for c in s:
            if len(mystack)!=0 and mystack[-1] == c:
                mystack.pop()
            else:
                mystack.append(c)

        return "".join(mystack)