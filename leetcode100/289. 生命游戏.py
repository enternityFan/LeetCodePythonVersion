#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：289. 生命游戏.py
@Author ：HuntingGame
@Date ：2023-02-08 19:36 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        利用了状态压缩的方法，来更高效的使用了int类型
        """
        n = len(board)
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                neighbors = self.neighbors(board,i,j)
                if neighbors == 3 or (board[i][j] == 1 and neighbors == 2):
                    self.set(board,i,j)
        for i in range(n):
            for j in range(m):
                board[i][j] = self.get(board,i,j)

    def neighbors(self,board,i,j):
        cnt = 0
        cnt += 1 if self.ok(board,i-1,j-1) else 0
        cnt += 1 if self.ok(board,i-1,j) else 0
        cnt += 1 if self.ok(board,i-1,j+1) else 0
        cnt += 1 if self.ok(board,i,j-1) else 0
        cnt += 1 if self.ok(board,i,j+1) else 0
        cnt += 1 if self.ok(board,i+1,j-1) else 0
        cnt += 1 if self.ok(board,i+1,j) else 0
        cnt += 1 if self.ok(board,i+1,j+1) else 0
        return cnt




    def ok(self,board,i,j):
        return i >=0 and i < len(board) and j >=0 and j < len(board[0]) and (board[i][j] & 1) == 1

    def set(self,board,i,j):
        board[i][j] |=2

    def get(self,board,i,j):
        return board[i][j] >> 1


