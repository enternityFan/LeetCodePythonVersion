#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：66. 加一.py
@Author ：HuntingGame
@Date ：2023-02-03 13:35 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n-1,-1,-1):
            if digits[i] < 9:
                digits[i] +=1
                return digits
            digits[i] = 0

        ans = [0] * (n+1)
        ans[0] = 1 # 全是9说明,不然for循环就挑出来了。
        return ans