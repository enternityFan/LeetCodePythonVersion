#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：48. 旋转图像.py
@Author ：HuntingGame
@Date ：2023-02-03 8:50 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        这个题只用有限几个变量就行了
        tR,tC是右上角点，dR,dC是左下角点
        """
        tR = 0
        tC = 0
        dR = len(matrix) - 1
        dC = len(matrix[0] ) - 1
        while tR < dR:
            """
            不同的框都转 
            """
            self.rotateEdge(matrix,tR,tC,dR,dC)
            tR+=1
            tC+=1
            dR-=1
            dC-=1

    def process(self,matrix,tR,tC,dR,dC):

        times = dC - tC
        tmp = 0
        for i in range(times):# i是组号的意思，每一组就是要互相转化的，比如说
            #123
            #456
            #789
            #1379是一组的，2468是一组的。
            tmp = matrix[tR][tC + i]
            matrix[tR][tC + i] = matrix[dR - i][tC]
            matrix[dR - i][tC] = matrix[dR][dC-i]
            matrix[dR][dC-i] = matrix[tR + i][dC]
            matrix[tR + i][dC] = tmp
