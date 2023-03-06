#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：剑指 Offer 12. 矩阵中的路径.py
@Author ：HuntingGame
@Date ：2023-03-06 18:22 
C'est la vie!!! enjoy ur day :D
'''
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        深度优先搜索，增加现场，，的问题。
        主逻辑就是测试每一个ij出发能不能返回True,如果能就返回True
        :param board:
        :param word:
        :return:
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.process(board,i,j,word,0):
                    return True

        return False

    def process(self,b,i,j,w,k):
        """
        目前到达了b[i][j],还有w[k...]没有搞定，
        :param b:
        :param i:
        :param j:
        :param w:
        :param k:
        :return:
        """
        if k == len(w):
            return True
        if (i < 0 or i == len(b) or j < 0 or j== len(b[0])):
            return False
        if b[i][j] !=w[k]:
            return False

        tmp = b[i][j]
        b[i][j] = 0#改为0，这样就可以保证不会走回头路了，当然改为123456789都行嘛，因为word仅有小写字母组成
        #模拟走上下左右
        ans = self.process(b,i-1,j,w,k+1) or self.process(b,i+1,j,w,k+1) or \
              self.process(b, i , j-1, w, k + 1) or self.process(b, i, j+1, w, k + 1)
        b[i][j] = tmp
        return ans

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
print(Solution().exist(board,"SSE"))