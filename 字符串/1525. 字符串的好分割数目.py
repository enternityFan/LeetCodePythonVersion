#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：1525. 字符串的好分割数目.py
@Author ：HuntingGame
@Date ：2022-11-08 8:48 
C'est la vie!!! enjoy ur day :D
'''
import collections


class Solution:
    def numSplits(self, s: str) -> int:
        n = len(s)
        dp = [[0]*3 for i in range(n)]

        dp[0][0] = 0
        dp[0][1] = len(set(s))
        dp[0][2] = 0
        cnts = collections.Counter(s)
        lset = set()
        rset = set(s)
        for i in range(1,n):
            if s[i-1] not in lset:
                dp[i][0] = dp[i-1][0] + 1

                lset.add(s[i-1])
            else:

                dp[i][0] = dp[i-1][0]
            cnts[s[i - 1]] -= 1
            if cnts[s[i-1]] == 0:
                rset.remove(s[i-1])
                dp[i][1] = dp[i-1][1] - 1
            else:
                dp[i][1] = dp[i-1][1]
            if dp[i][1] == dp[i][0]:
                dp[i][2] = dp[i-1][2] +1
            else:
                dp[i][2] = dp[i-1][2]

        return dp[-1][2]


print(Solution().numSplits("aacaba"))