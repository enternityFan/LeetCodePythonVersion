#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：42. 接雨水.py
@Author ：HuntingGame
@Date ：2022-11-18 9:07 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        lmax = height[0]
        rmax = height[-1]
        ans = [0] * len(height)
        l = 1
        r = n -2
        while (l < r):
            if lmax > rmax:
                ans[r] = max(0,rmax - height[r])
                rmax = max(rmax,height[r])
                r -=1
            else:
                ans[l] = max(0,lmax - height[l])
                lmax = max(lmax,height[l])
                l +=1

        return sum(ans)


