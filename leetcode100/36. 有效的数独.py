#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：36. 有效的数独.py
@Author ：HuntingGame
@Date ：2023-02-02 11:47 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row = [[False for _ in range(10)] for i in range (9)]#row[i][j]表示第i行是否出现过j
        col = [[False for _ in range(10)] for i in range (9)]#同上
        bucket = [[False for _ in range(10)] for i in range (9)]#同上，这个是小方框是否出现过。

        for i in range(9):
            for j in range(9):
                bid = 3 * (i //3 ) + (j // 3)
                if board[i][j] !='.':
                    num = int(board[i][j])
                    if row[i][num] or col[j][num] or bucket[bid][num]:
                        return False
                    row[i][num] = True
                    col[j][num] = True
                    bucket[bid][num] = True

        return True









