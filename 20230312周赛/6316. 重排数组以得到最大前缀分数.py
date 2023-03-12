#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：6316. 重排数组以得到最大前缀分数.py
@Author ：HuntingGame
@Date ：2023-03-12 10:32 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse=True)

        prefix = [nums[0]]
        if prefix[0] <=0:
            return 0
        ans = 1
        for i in range(1,len(nums)):
            prefix.append(prefix[-1] + nums[i])
            if prefix[-1] > 0:
                ans +=1
            else:
                break
        print(prefix)
        return ans

