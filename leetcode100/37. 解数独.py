#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：37. 解数独.py
@Author ：HuntingGame
@Date ：2023-02-02 12:08 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row,col,bucket = self.initMaps(board)
        self.process(board,0,0,row,col,bucket)
        print(bucket)




    def initMaps(self,board):
        """
        返回初始的地图
        :return:
        """
        row = [[False for _ in range(10)] for i in range (9)]#row[i][j]表示第i行是否出现过j
        col = [[False for _ in range(10)] for i in range (9)]#同上
        bucket = [[False for _ in range(10)] for i in range (9)]#同上，这个是小方框是否出现过。

        for i in range(9):
            for j in range(9):
                bid = 3 * (i //3 ) + (j // 3)
                if board[i][j] !='.':
                    num = int(board[i][j])
                    row[i][num] = True
                    col[j][num] = True
                    bucket[bid][num] = True

        return row,col,bucket

    def process(self,board,i,j,row,col,bucket):
        if i == 9:
            #全部填完了，返回True
            print("find")
            return True

        nexti = i if j !=8 else i+1
        nextj = j+1 if j !=8 else 0
        if board[i][j] !='.':
            #说明这个地方是有数字的,那就处理下一个空
            return self.process(board,nexti,nextj,row,col,bucket)
        else:
            bid = 3 * (i // 3) + (j // 3)
            for num in range(1,10):
                if (not row[i][num]) and(not col[j][num]) and (not bucket[bid][num]):
                    row[i][num] = True
                    col[j][num] = True
                    bucket[bid][num] = True
                    board[i][j] = str(num)
                    if self.process(board,nexti,nextj,row,col,bucket):
                        return True
                    row[i][num] = False
                    col[j][num] = False
                    bucket[bid][num] = False
                    board[i][j] = "."
        #print("no")
        return False




board=[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
print(Solution().solveSudoku(board))








