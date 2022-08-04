# @Time : 2022-08-04 19:07
# @Author : Phalange
# @File : 2221. 数组的三角和.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        while n!=1:
            newNums = []
            for i in range(0,n-1):
                newNums.append((nums[i] + nums[i+1]) % 10)
            nums = newNums
            n = len(nums)


        return nums[0]