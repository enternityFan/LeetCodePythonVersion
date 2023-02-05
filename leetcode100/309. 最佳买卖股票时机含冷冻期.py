#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：309. 最佳买卖股票时机含冷冻期.py
@Author ：HuntingGame
@Date ：2023-02-05 13:37 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        这个代码是原始代码的空间优化后的版本
        [i]不参与；
        [i]参与，B[i-1]+[i],B表示0到i-2上做无限次交易，再结合一个最后一次买入的。
        :param prices:
        :return:
        """
        if len(prices) < 2:
            return 0

        buy1 = max(-prices[0],-prices[1])
        sell1 = max(0,prices[1] - prices[0])
        sell2 = 0
        for i in range(2,len(prices)):
            tmp = sell1
            sell1 = max(sell1,buy1 + prices[i])
            buy1 = max(buy1,sell2 - prices[i])
            sell2 = tmp

        return sell1






