#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：32. 最长有效括号.py
@Author ：HuntingGame
@Date ：2022-11-16 19:41 
C'est la vie!!! enjoy ur day :D
'''
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if s == "" or len(s) == 1:
            return 0
        n = len(s)
        dp = [0] * n
        ans = 0
        prev = 0
        for i in range(1,n):
            if s[i] == ")":
                prev = i - dp[i-1] - 1# 与s[i]配对的（的左边的哪个位置
                if prev >= 0 and s[prev] == "(":
                    dp[i] = 2 + dp[i-1] + (dp[prev-1] if prev else 0)
            ans = max(ans,dp[i])

        return ans

print(Solution().longestValidParentheses(")()())"))
