# @Time : 2022-08-09 17:42
# @Author : Phalange
# @File : 1877. 数组中最大数对和的最小值.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        """
         “最大数对和最小”就是在这个数组的一系列数对组合中，找到那个最小的最大数对和
        :param nums:
        :return:
        """
        nums.sort()
        nums2 = []
        n = len(nums)
        for i in range(n//2):
            nums2.append(nums[i] + nums[n-1-i])
        return max(nums2)