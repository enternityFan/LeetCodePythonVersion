#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：322. 零钱兑换.py
@Author ：HuntingGame
@Date ：2023-02-09 18:55 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        dp[i][j]表示自由用arr[0...i]的所有钱，拼出j元最少的张数J
        1)使用0张[i]位置的钱，那就是dp[i-1][j]
        2)1张i位置的钱，那就是dp[i][j-i] +1
        3)2张i位置的钱，那就是dp[i][j-2i] +2
        .
        .
        .
        只要不超边界，就枚举以上求最小。





        :param coins:
        :param amount:
        :return:
        """
        if len(coins) == 0:
            return -1
        N = len(coins)
        dp = [[0 for _ in range(amount + 1)] for i in range (N)]
        #dp[i][0] = 0
        #dp[0][j] = arr[0]的整数倍，有张数，倍数，其他的格子填-1
        for j in range(1,amount+1):
            if j % coins[0] !=0:
                dp[0][j] = -1
            else:
                dp[0][j] = j // coins[0]

        #普遍情况
        for i in range(1,N):
            for j in range(1,amount+1):
                dp[i][j] = amount+1 #表示一个大的值,相当于inf
                if dp[i-1][j] !=-1:
                    dp[i][j] = dp[i-1][j]

                if j - coins[i] >=0 and dp[i][j-coins[i]] !=-1:
                    dp[i][j] = min(dp[i][j],dp[i][j-coins[i]]+1)

                if dp[i][j] == amount +1:
                    #表示还是无效的
                    dp[i][j] = -1
        return dp[N-1][amount]


print(Solution().coinChange([1,2,5],11))