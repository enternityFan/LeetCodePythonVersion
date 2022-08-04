# @Time : 2022-08-04 19:02
# @Author : Phalange
# @File : 1689. 十-二进制数的最少数目.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D



class Solution:
    def minPartitions(self, n: str) -> int:
        ans = 0
        if len(n) ==1:
            return int(n)
        else:
            return int(max(n))