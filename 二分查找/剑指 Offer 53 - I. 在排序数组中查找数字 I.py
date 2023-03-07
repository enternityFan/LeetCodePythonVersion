#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：剑指 Offer 53 - I. 在排序数组中查找数字 I.py
@Author ：HuntingGame
@Date ：2023-03-07 13:25 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums == []:
            return 0
        L = 0
        R = len(nums) - 1
        ans = 0
        mid = 0
        while L <= R:
            mid = L + ((R - L ) >> 1)

            if nums[mid] == target:
                break
            elif nums[mid ] < target:
                L = mid + 1
            else:
                R = mid - 1
        if L >R:
            return ans
        print(mid)
        mid2 = mid
        ans =1
        while mid2 >-1 and nums[mid2] ==target:
            ans +=1
            mid2 -=1
        mid2 = mid
        while mid2 < len(nums) and nums[mid2] ==target:
            ans +=1
            mid2 +=1
        return ans-2

print(Solution().search([1],1))

