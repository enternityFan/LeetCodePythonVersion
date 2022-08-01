# @Time : 2022-08-01 11:01
# @Author : Phalange
# @File : 剑指 Offer II 076. 数组中的第 k 大的数字.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        return heapq.nlargest(k,nums).pop()
