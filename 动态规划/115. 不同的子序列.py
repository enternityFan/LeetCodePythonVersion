#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：115. 不同的子序列.py
@Author ：HuntingGame
@Date ：2022-12-23 17:08 
C'est la vie!!! enjoy ur day :D
'''

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)

        dp = [[0] * (n+1)  for _ in range(m+1)]

        for i in range(m+1):
            # 填第一行
            dp[i][0] = 1 # t的长度为0，那么肯定有一种方案
        for i in range(n+1):
            dp[0][i] = 0 # s的长度为0，肯定不行

        for i in range(m+1):

            for j in range(n+1):

                dp[i][j] = dp[i-1][j] + (dp[i-1][j-1] if s[i-1] == t[j-1] else 0)

        return dp[-1][-1]


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)

        dp = [0] * (n + 1)

        dp[0] = 1

        for i in range(1, m + 1):

            for j in range(n,0,-1):# 这里从后往前，我的理解是，因为我只有考虑好I这个的位置时，才去看前面的。
                #print(j)
                if s[i - 1] == t[j - 1]:
                    dp[j] += dp[j - 1]


        return dp[-1]


s = "rabbbit"
t = "rabbit"
print(Solution().numDistinct(s,t))