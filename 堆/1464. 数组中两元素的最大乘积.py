# @Time : 2022-08-01 10:49
# @Author : Phalange
# @File : 1464. 数组中两元素的最大乘积.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List

import heapq
class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        a,b = heapq.nlargest(2,nums)
        return (a-1) * (b-1)
