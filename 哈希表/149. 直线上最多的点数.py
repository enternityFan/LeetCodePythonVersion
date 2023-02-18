#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：149. 直线上最多的点数.py
@Author ：HuntingGame
@Date ：2022-12-16 12:56 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <=2:
            return n
        alpha = {} # 斜率表
        result = 0
        for i in range(n):
            alpha.clear()
            sP = 1 # 相同的点数
            sX = 0 #共X
            sY = 0 #共Y
            line = 0
            for j in range(i+1,n):
                if points[i][0] == points[j][0] and points[i][1] == points[j][1]:
                    sP +=1
                elif points[i][0] == points[j][0]:
                    sX +=1
                elif points[i][1] == points[j][1]:
                    sY +=1

                else:
                    max_gcd = self.gcd(points[i][0] - points[j][0],points[i][1] - points[j][1])
                    key = str((points[i][0]-points[j][0]) // max_gcd) + "_" + str((points[i][1]-points[j][1]) // max_gcd)
                    if key not in alpha:
                        alpha[key] = 0
                    alpha[key] +=1
                    line = max(line,alpha[key])



            result = max(result,sP+max(line,max(sX,sY)))
        return result

    def gcd(self,a,b):

        return a if b == 0 else self.gcd(b,a%b)

print(Solution().maxPoints([[1,1,],[2,2],[3,3]]))