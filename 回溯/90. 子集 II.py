#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/10/24 21:48
# @Author  : HuntingGame
# @FileName: 90. 子集 II.py
# @Software: PyCharm
# C'est la vie. Enjoy ur day ! :D
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def back_tracking(temp, start):
            res.append(temp[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                temp.append(nums[i])
                back_tracking(temp, i+1)
                temp.pop()
        back_tracking([], 0)
        return res


print(Solution().subsetsWithDup([1,2,2]))