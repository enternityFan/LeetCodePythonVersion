#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：剑指 Offer II 094. 最少回文分割.py
@Author ：HuntingGame
@Date ：2022-11-24 21:23 
C'est la vie!!! enjoy ur day :D
'''


class Solution:
    def minCut(self, s: str) -> int:

        n = len(s)
        if n == 1:
            return 0

        isP = [[False] * n for _ in range(n)]

        # 填对角线元素
        for i in range(n):
            isP[i][i] = True
        # 填对角线元素上面的元素
        for i in range(0,n-1):
            isP[i][i+1] = True if s[i] == s[i+1] else False

        # 开始填表
        for i in range(n-3,-1,-1):
            for j in range(i+2,n):
                #i为行，j为列
                isP[i][j] = (s[i]==s[j]) & (isP[i+1][j-1])

        dp = [100000] * (n+1)
        dp[n] = 0
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if isP[i][j]:
                    dp[i] = min(dp[i],1+dp[j+1])

        return dp[0]-1

print(Solution().minCut("abakfkeaec"))