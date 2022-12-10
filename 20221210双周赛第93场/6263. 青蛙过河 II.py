#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：6263. 青蛙过河 II.py
@Author ：HuntingGame
@Date ：2022-12-10 22:45 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def maxJump(self, stones: List[int]) -> int:
        stones.append(stones[0])
        ans = 0
        for i in range(1,len(stones)):
            ans = max(ans,stones[i] - stones[i-1])
        return ans