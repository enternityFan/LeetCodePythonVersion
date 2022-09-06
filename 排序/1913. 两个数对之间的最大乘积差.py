# @Time : 2022-09-06 19:29
# @Author : Phalange
# @File : 1913. 两个数对之间的最大乘积差.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        return nums[-1] * nums[-2] - nums[0] * nums[1]