#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：334. 递增的三元子序列.py
@Author ：HuntingGame
@Date ：2023-02-09 20:04 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        """
        O(n)时间复杂度，O(1)空间复杂度。
        很牛逼，用二分
        :param nums:
        :return:
        """
        if len(nums) < 3:
            return False

        ends =[0,0,0]
        ends[0] = nums[0]
        right = 0
        l = 0
        r = 0
        m = 0
        for i in range(1,len(nums)):
            l = 0
            r = right
            while  l <= r:
                m = (l + r) // 2
                if nums[i] > ends[m]:
                    l = m +1
                else:
                    r = m - 1
            right = max(right,l)
            if right > 1:
                return True
            ends[l] = nums[i]
        return False




