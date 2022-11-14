#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：477. 汉明距离总和.py
@Author ：HuntingGame
@Date ：2022-11-14 9:40 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        """
        统计一下每一位上0的个数，每一位上1的个数
        c * (n - c)

        """
        ans = 0
        tmp = [0] * 32
        tmp2 = [0] * 32
        for i in range(len(nums)):
            for j in range(32):

                if nums[i] & (2 ** j):
                    tmp[j] +=1
                else:
                    tmp2[j] +=1

        for i in range(32):

            ans += tmp[i] * tmp2[i]



        return ans

print(Solution().totalHammingDistance([4,14,2]))