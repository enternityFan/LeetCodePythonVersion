#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：130. 被围绕的区域.py
@Author ：HuntingGame
@Date ：2023-02-06 9:17 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        """
        Do not return anything, modify board in-place instead.
        """
        ans = [False]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    ans[0] = True
                    self.can(board,i,j,ans)
                    board[i][j] = 'T' if ans[0] else 'F'
        for i in range(len(board)):
            for j in range(len(board[0])):
                can = board[i][j]
                if can == "T" or can == "F":
                    board[i][j] = '.'
                    self.change(board,i,j,can)



    def can(self,board,i,j,ans):

        if i < 0 or i == len(board) or j < 0 or j == len(board[0]):
            #越界
            ans[0] = False
            return

        if board[i][j] == "O":
            board[i][j] = "."
            self.can(board,i-1,j,ans)
            self.can(board,i+1,j,ans)
            self.can(board,i,j-1,ans)
            self.can(board,i,j+1,ans)


    def change(self,board,i,j,can):
        if i < 0 or i == len(board) or j < 0 or j == len(board):
            return
        if board[i][j] == ".":
            board[i][j] = 'X' if can == 'T' else 'O'
            self.change(board,i-1,j,can)
            self.change(board,i+1,j,can)
            self.change(board,i,j-1,can)
            self.change(board,i,j+1,can)










