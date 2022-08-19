# @Time : 2022-08-19 11:03
# @Author : Phalange
# @File : 414. 第三大的数.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import heapq
from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        heapq.heapify(nums)
        if len(nums) < 3:
            res = heapq.nlargest(1,nums)
        else:
            res = heapq.nlargest(3,nums)
        return res[-1]
print(Solution().thirdMax([2,2,3,1]))