# @Time : 2022-08-13 18:05
# @Author : Phalange
# @File : 1991. 找到数组的中间位置.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        allSum = sum(nums)
        for i in range(n):
            if sum(nums[:i])*2 == allSum - nums[i]:
                return i

        return -1


