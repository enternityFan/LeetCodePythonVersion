#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：2554. 从一个范围内选择最多整数 I.py
@Author ：HuntingGame
@Date ：2023-03-12 13:00 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        bs =  set(banned)
        ans = 0
        tmp = 0

        for i in range(n+1):
            if i in bs:
                continue
            if i + tmp <=maxSum:
                tmp +=i
                ans +=1
            else:
                break
        return ans









