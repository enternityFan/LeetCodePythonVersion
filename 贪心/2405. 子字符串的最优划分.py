# @Time : 2022-09-18 11:42
# @Author : Phalange
# @File : 2405. 子字符串的最优划分.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import collections


class Solution:
    def partitionString(self, s: str) -> int:
        ans = 0
        subs = ""
        for c in s:
            if c in subs:
                ans +=1
                subs = c
            else:
                subs +=c

        return ans

