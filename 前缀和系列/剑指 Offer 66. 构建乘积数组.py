# @Time : 2022-07-30 19:38
# @Author : Phalange
# @File : 剑指 Offer 66. 构建乘积数组.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        lres = 1 #左边的累乘
        rres = 1 #右边的累乘

        res = [0] * len(a)
        for i in range(len(a)):

            res[i] =lres
            lres *= a[i]

        for i in range(len(a)-1,-1,-1):

            res[i] *=rres
            rres *= a[i]
        return res

print(Solution().constructArr([1,2,3,4,5]))