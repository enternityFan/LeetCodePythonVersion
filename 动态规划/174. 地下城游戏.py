#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：174. 地下城游戏.py
@Author ：HuntingGame
@Date ：2022-12-23 20:43 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:

        def process(matrix,N,M,row,col):
            if row == N-1 and col == M - 1:
                return -matrix[-1][-1]+1  if matrix[-1][-1] < 0 else 1

            if row == N - 1:
                rightNeed = process(matrix,N,M,row,col+1)
                if matrix[row][col] < 0:
                    return -matrix[row][col] + rightNeed
                elif matrix[row][col] >= rightNeed:
                    return 1
                else:
                    return rightNeed - matrix[row][col]

            if col == M - 1:
                downNeed = process(matrix,N,M,row+1,col)
                if matrix[row][col] < 0:
                    return -matrix[row][col] + downNeed
                elif matrix[row][col] >= downNeed:
                    return 1
                else:
                    return downNeed - matrix[row][col]

            # 不然的话，就是可以往下走往右走
            minNextNeed = min(process(matrix,N,M,row,col+1),process(matrix,N,M,row+1,col))
            if matrix[row][col] < 0:
                return -matrix[row][col] + minNextNeed
            elif matrix[row][col] >= minNextNeed:
                return 1
            else:
                return minNextNeed - matrix[row][col]

        return process(dungeon,len(dungeon),len(dungeon[0]),0,0)


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:

        N = len(dungeon)
        M = len(dungeon[0])
        if N == 0 or M == 0:
            return 1



        dp = [[0] * N for _ in range(M)]
        dp[N][M] = 1 if dungeon[N][M] > 0 else -dungeon[N][M] + 1











