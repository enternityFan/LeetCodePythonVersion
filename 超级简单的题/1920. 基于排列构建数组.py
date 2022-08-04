# @Time : 2022-08-04 18:49
# @Author : Phalange
# @File : 1920. 基于排列构建数组.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[nums[i]] for i in range(len(nums))]