#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：123. 买卖股票的最佳时机 III.py
@Author ：HuntingGame
@Date ：2023-02-05 11:43 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        i位置为卖出时机，就是在i位置的时候是第二次交易的卖出时间。
        那么其实需要知道0到i-1要实现一次最大的交易，同时知道有一个最佳的买入时机,那其实想要的就是 ：
         做完一个交易并且减去买入价格的最大值。
        :param prices:
        :return:
        """
        if len(prices) < 2:
            return 0
        ans = 0
        doneOnceMinusBuyMax = -prices[0] #交易一次减去买入指标的最大
        doneOnceMax = 0#一次交易的最大值
        minval = prices[0]
        for i in range(1,len(prices)):
            minval = min(minval,prices[i])
            ans = max(ans,doneOnceMinusBuyMax + prices[i]) #完成两次交易
            doneOnceMax = max(doneOnceMax,prices[i] - minval)
            doneOnceMinusBuyMax = max(doneOnceMinusBuyMax,doneOnceMax - prices[i])

        return ans


