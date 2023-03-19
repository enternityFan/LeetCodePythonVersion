#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：6324. 最大化数组的伟大值.py
@Author ：HuntingGame
@Date ：2023-03-18 23:00 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        a = sorted(nums)
        cnts = {}
        ans = 0
        j = 0
        i = 0
        while j < len(nums):
            if a[j] > a[i]:
                ans +=1
                i +=1

            j +=1

        print(a)
        return ans

print(Solution().maximizeGreatness([1,3,5,2,1,3,1]))
print(Solution().maximizeGreatness([1,2,4,10,1,2,2,2,2,2,2,2,2]))


