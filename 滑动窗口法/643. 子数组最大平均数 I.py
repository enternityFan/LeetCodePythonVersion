#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：643. 子数组最大平均数 I.py
@Author ：HuntingGame
@Date ：2022-11-22 9:27 
C'est la vie!!! enjoy ur day :D
'''
import collections
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = 0.0
        n = len(nums)
        if n ==k:
            return sum(nums) / n

        windows = nums[:k]
        windows = collections.deque(windows)
        ans = sum(windows)
        cur = sum(windows)
        for i in range(k,len(nums)):
            windows.popleft()
            windows.append(nums[i])
            print(nums[i-k])
            cur = cur - nums[i-k] + nums[i]
            ans = max(ans,cur)
            print(ans)

        return ans / k

print(Solution().findMaxAverage([0,4,0,3,2],1))