#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：34.在排序数组中查找元素的第一个和最后一个位置.py
@Author ：HuntingGame
@Date ：2023-02-02 11:41 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        两个二分就是想了。
        :param nums:
        :param target:
        :return:
        """
        ans = [-1,-1]
        if len(nums) == 0:
            return ans

        ans[0] = self.findFirst(nums,target)
        ans[1] = self.findLast(nums,target)

        return ans


    def findFirst(self,nums,target):
        L = 0
        R = len(nums) - 1
        ans = -1
        mid = 0
        while L <=R:
            mid = L + ((R - L ) >>1)
            if nums[mid ] == target:
                ans = mid
                R = mid - 1# 继续往左边找
            elif nums[mid] < target:
                L = mid + 1
            else:
                R = mid - 1

        return ans

    def findLast(self, nums, target):
        L = 0
        R = len(nums) - 1
        ans = -1
        mid = 0
        while L <= R:
            mid = L + ((R - L) >> 1)
            if nums[mid] == target:
                ans = mid
                L = mid + 1 #继续往右边找
            elif nums[mid] < target:
                L = mid + 1
            else:
                R = mid - 1

        return ans

