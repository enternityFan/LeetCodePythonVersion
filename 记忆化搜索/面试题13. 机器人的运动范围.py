#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：面试题13. 机器人的运动范围.py
@Author ：HuntingGame
@Date ：2023-03-07 18:02 
C'est la vie!!! enjoy ur day :D
'''
import math


class Solution:
    def __init__(self):
        self.ans = 0



    def movingCount(self, m: int, n: int, k: int) -> int:
        mymap = [[-1 for _ in range(n)] for i in range(m)]
        self.process(0,0,m,n,k,mymap)
        return self.ans

    def process(self,i,j,m,n,k,mymap):
        """
        当前位置在i,j可以往哪个方向移动，
        :param i:
        :param j:
        :param m:
        :param n:
        :param k:
        :return:
        """
        if i < 0 or i >=m or j < 0 or j >= n:
            return
        if mymap[i][j] == 0:
            return #来过了
        if self.get(i,j) > k:
            return

        self.ans +=1 #可以到达这个格子
        mymap[i][j] = 0 #表示已经到达了
        self.process(i+1,j,m,n,k,mymap)
        self.process(i,j+1,m,n,k,mymap)
        self.process(i-1,j,m,n,k,mymap)
        self.process(i,j-1,m,n,k,mymap)

    def get(self,i,j):
        tmp = 0
        while i:
            tmp +=i % 10
            i //=10
        while j:
            tmp +=j % 10
            j //=10
        return tmp



