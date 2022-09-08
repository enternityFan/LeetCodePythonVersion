# @Time : 2022-09-08 20:12
# @Author : Phalange
# @File : 剑指 Offer 57. 和为s的两个数字.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        l = 0
        r = len(nums)-1
        while l <=r:
            ans = nums[l] + nums[r]
            if ans > target:
                r = r - 1
            elif ans < target:
                l = l + 1
            else:
                break

        return [nums[l],nums[r]]
