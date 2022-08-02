# @Time : 2022-08-01 22:25
# @Author : Phalange
# @File : 面试题 17.14. 最小K个数.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import heapq
from typing import List


class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        return heapq.nsmallest(k,arr)