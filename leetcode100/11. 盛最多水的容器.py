#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：11. 盛最多水的容器.py
@Author ：HuntingGame
@Date ：2023-02-01 14:24 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        遍历一遍就行了,左右两侧一起移动，哪边小结算哪一册。
        这种求解思路不去想每个杆的最优解，而是让答案尽可能的大
        :param height:
        :return:
        """
        l = 0
        r = len(height) - 1
        ans = 0
        while l < r:
            ans = max(ans,min(height[l],height[r]) * (r - l))
            if height[l] > height[r]:
                r -=1
            else:
                l +=1

        return ans

