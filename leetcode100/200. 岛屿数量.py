#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：200. 岛屿数量.py
@Author ：HuntingGame
@Date ：2023-02-07 21:19 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        就是一个感染的过程，注意要修改现场
        :param grid:
        :return:
        """
        N = len(grid)
        M = len(grid[0])
        res = 0
        for i in range(N):
            for j in range(M):
                if grid[i][j] == "1":
                    res +=1
                    self.infect(grid,i,j,N,M)

        return res


    def infect(self,m,i,j,N,M):
        if i < 0 or i >=N or j < 0 or j >=M or m[i][j] !="1":
            return
        m[i][j] = '2'
        self.infect(m,i+1,j,N,M)
        self.infect(m,i-1,j,N,M)
        self.infect(m,i,j+1,N,M)
        self.infect(m,i,j-1,N,M)




