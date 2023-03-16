#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：1237. 找出给定方程的正整数解.py
@Author ：HuntingGame
@Date ：2023-03-16 22:07 
C'est la vie!!! enjoy ur day :D
'''
"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):

"""
class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:

        ans = []
        y = 1000
        for x in range(1,1001):
            while y and customfunction.f(x,y) >z:
                y -=1
            if y == 0:
                break
            if customfunction.f(x,y) == z:
                ans.append([x,y])
        return ans




class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        """
        枚举的做法，最后一个实例会超时,不过我通过添加break的方法优化后，不超时了。
        :param customfunction:
        :param z:
        :return:
        """
        ans = []
        for i in range(1, 1001):
            for j in range(1, 1001):
                if customfunction.f(i, j) == z:
                    ans.append([i, j])
                elif customfunction.f(i,j) > z:
                    break

        return ans




