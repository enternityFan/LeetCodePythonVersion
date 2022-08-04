# @Time : 2022-08-04 9:50
# @Author : Phalange
# @File : 1403. 非递增顺序的最小子序列.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import heapq
from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums = sorted(nums,reverse=True)

        tmp = sum(nums)
        idx = 0
        tmp2 = 0
        for i in range(len(nums)):
            tmp2 +=nums[i]
            tmp -=nums[i]
            if tmp2 > tmp:
                idx = i
                break
        return nums[:idx+1]

