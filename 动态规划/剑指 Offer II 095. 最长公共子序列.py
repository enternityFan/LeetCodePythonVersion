#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：剑指 Offer II 095. 最长公共子序列.py
@Author ：HuntingGame
@Date ：2022-11-22 8:08 
C'est la vie!!! enjoy ur day :D
'''


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2 or text1 == "" or text2 == "":
            return 0
        n = len(text1)
        m = len(text2)
        dp = [[0] * m for i in range(n)]
        if text1[0] == text2[0] :
            dp[0][0] =1

        for i in range(1,n):
            dp[i][0] = 1 if text2[0] == text1[i] else dp[i-1][0]

        for i in range(1,m):
            dp[0][i] = 1 if text2[i] == text1[0] else dp[0][i-1]

        for i in range(1,n):
            for j in range(1,m):
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
                if text1[i] == text2[j]:
                    dp[i][j] = max(dp[i-1][j-1]+1,dp[i][j])

        return dp[-1][-1]

text1 = "abcde"
text2 = "ace"
print(Solution().longestCommonSubsequence(text1,text2))

