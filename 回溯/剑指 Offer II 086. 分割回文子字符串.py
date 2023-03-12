#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：剑指 Offer II 086. 分割回文子字符串.py
@Author ：HuntingGame
@Date ：2023-03-12 10:11 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        dp = self.getDP(s)
        path = []
        ans = []
        self.process(s,0,path,dp,ans)
        return ans

    def getDP(self,s):
        N = len(s)
        dp = [[False for _ in range(N) ] for i in range(N)]
        for i in range(N-1):
            dp[i][i] = True
            dp[i][i+1] = (s[i] == s[i+1])
        dp[N-1][N-1] = True
        for j in range(2,N):
            row = 0
            col = j
            while row < N and col < N:
                dp[row][col] = (s[row] == s[col] and dp[row+1][col-1])
                row +=1
                col +=1

        return dp
    def process(self,s,idx,path,dp,ans):
        if idx == len(s):
            ans.append(path.copy())
        else:
            for end in range(idx,len(s)):
                if dp[idx][end]:
                    #可以组成回文
                    path.append(s[idx:end+1])
                    self.process(s,end+1,path,dp,ans)
                    path.pop()