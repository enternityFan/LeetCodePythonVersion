#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：84.柱状图中最大的矩形.py
@Author ：HuntingGame
@Date ：2023-02-03 18:34 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        这个不是原始的单调栈
        :param heights:
        :return:
        """
        if heights == []:
            return 0
        mystack = []
        maxArea = 0
        for i in range(len(heights)):
            while mystack !=[] and heights[i] <= heights[mystack[-1]]:#这个等号就很有意思了。他的意思就是我当前求得答案不需要必须是最优的，只要保证之前和之后都不会错过最优就行，这是很难的一种思路。
                j = mystack.pop()
                k = -1 if mystack == [] else mystack[-1]
                curArea = (i-k-1) * heights[j]
                maxArea = max(maxArea,curArea)
            mystack.append(i)

        while mystack !=[]:
            j = mystack.pop()
            k = -1 if mystack == [] else mystack[-1]
            curArea = (len(heights) - k - 1) * heights[j]
            maxArea = max(maxArea, curArea)
        return maxArea

