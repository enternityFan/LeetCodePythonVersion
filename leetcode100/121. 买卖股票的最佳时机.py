#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：121. 买卖股票的最佳时机.py
@Author ：HuntingGame
@Date ：2023-02-05 11:27 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans= -prices[0]
        minval = prices[0]
        for i in range(1,len(prices)):
            ans = max(ans,prices[i] - minval)
            minval = min(minval,prices[i])


        return ans