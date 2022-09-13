# @Time : 2022-09-13 13:36
# @Author : Phalange
# @File : 1903. 字符串中的最大奇数.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D


class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = len(num)
        ans = ""
        for i in range(n-1,-1,-1):
            if num[i] in "13579":
                ans = num[:i+1]
                break

        return ans