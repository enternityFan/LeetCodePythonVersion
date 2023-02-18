#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：122. 买卖股票的最佳时机 II.py
@Author ：HuntingGame
@Date ：2023-02-05 11:39 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        ans = 0
        for i in range(1,len(prices)):
            ans +=max(prices[i] - prices[i-1],0)

        return ans