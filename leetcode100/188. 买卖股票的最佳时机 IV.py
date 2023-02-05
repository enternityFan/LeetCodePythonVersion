#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：188. 买卖股票的最佳时机 IV.py
@Author ：HuntingGame
@Date ：2023-02-05 13:10 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        """
        这个是有枚举行为的dp版本，过不了的，得优化下。看下面的代码
        这个题有一个大的过滤的，如果k>N/2,就等同于无限次的，因为他们的本质是一样的，那这其实就类似于问题2的。
        不然的话就是dp；dp[i][j]代表智能在0到i上，最大交易次数不超过J,的最大收益
        dp[N-1][K]的值就是答案。
        很明显dp[0][..]和dp[..][0]都是0的
        对于任意的[i][j]:
        1)如果[i]不参加任何交易，dp[i][j] = dp[i-1][j]
        2)[i]参加的是最后一次交易的卖出时机。
        2.1）最后买入[i]
        2.2）最后买入[i-1]
        2.3)。。。最后买入[i-2]
        枚举下来。
        2)总结来说的话就是max{dp[k][j-1]+[i]-[k],k属于[0,i]}
        :param k:
        :param prices:
        :return:
        """
        if len(prices) == 0:
            return 0
        N = len(prices)
        if k >= N/2:
            return self.allTrans(prices)

        dp = [[0 for _ in range(k+1)] for i in range (N)]
        #dp[0][...]和dp[..][0]都是0的
        for i in range(1,N):
            for j in range(1,k+1):
                #1) [i]不参与
                dp[i][j] = dp[i-1][j]
                #2) 枚举
                for p in range(0,i+1):
                    dp[i][j] = max(dp[p][j-1] + prices[i] - prices[p],dp[i][j])


        return dp[N-1][k]




    def allTrans(self,prices):
        """

        :param arr:
        :return:

        """
        ans = 0
        for i in range(1,len(prices)):
            ans +=max(prices[i] - prices[i-1],0)

        return ans


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        """
        斜率优化后的。
        :param k:
        :param prices:
        :return:
        """
        if len(prices) == 0:
            return 0
        N = len(prices)
        if k >= N/2:
            return self.allTrans(prices)
        ans = 0
        dp = [[0 for _ in range(N)] for i in range (k+1)]
        #dp[0][...]和dp[..][0]都是0的

        for tran in range(1, k + 1):
            pre = dp[tran][0]
            best = pre - prices[0]
            for index in range(1, N):
                pre = dp[tran - 1][index]
                dp[tran][index] = max(dp[tran][index - 1], prices[index] + best)
                best = max(best, pre - prices[index])
                ans = max(dp[tran][index], ans)


        return ans

    def allTrans(self,prices):
        """

        :param arr:
        :return:

        """
        ans = 0
        for i in range(1,len(prices)):
            ans +=max(prices[i] - prices[i-1],0)

        return ans








