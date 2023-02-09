#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：329. 矩阵中的最长递增路径.py
@Author ：HuntingGame
@Date ：2023-02-09 19:43 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """
        这个题进阶班其实讲过。。
        :param matrix:
        :return:
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        ans = 0
        N = len(matrix)
        M = len(matrix[0])
        dp = [[1 for _ in range(M)] for i in range (N)]
        for i in range(N):
            for j in range(M):
                ans = max(ans,self.lip(matrix,i,j,dp))

        return ans

    def lip(self,matrix,i,j,dp):
        if dp[i][j] !=0:
            return dp[i][j]

        next = 0
        if self.canWalk(matrix,i,j,i-1,j):
            next = max(next,self.lip(matrix,i-1,j,dp))

        if self.canWalk(matrix,i,j,i+1,j):
            next = max(next,self.lip(matrix,i+1,j,dp))

        if self.canWalk(matrix, i, j, i, j-1):
            next = max(next, self.lip(matrix, i , j-1, dp))

        if self.canWalk(matrix, i, j, i, j+1):
            next = max(next, self.lip(matrix, i, j+1, dp))

        dp[i][j] = 1 + next
        return dp[i][j]



    def canWalk(self,matrix,i1,j1,i2,j2):
        return i2 >=0 and i2 < len(matrix) and j2 >=0 and j2 < len(matrix[0]) \
            and matrix[i1][j1] < matrix[i2][j2]