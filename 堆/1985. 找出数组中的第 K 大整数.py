# @Time : 2022-08-01 22:28
# @Author : Phalange
# @File : 1985. 找出数组中的第 K 大整数.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import heapq
from typing import List


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        return str(heapq.nlargest(k,nums,key=lambda x:int(x)).pop())