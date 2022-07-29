# @Time : 2022-07-29 21:45
# @Author : Phalange
# @File : 2215. 找出两数组的不同.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List
import collections

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        nums1 = set(nums1)
        nums2 = set(nums2)
        n1 = []
        n2 = []
        for each in nums1:
            if each not in nums2:
                n1.append(each)

        for each in nums2:
            if each not in nums1:
                n2.append(each)
        return [n1,n2]
