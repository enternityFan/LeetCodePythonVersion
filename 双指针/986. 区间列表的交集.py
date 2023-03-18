#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：986. 区间列表的交集.py
@Author ：HuntingGame
@Date ：2023-03-18 21:32 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if firstList == [] or secondList == []:
            return []
        i = 0
        j = 0
        ans = []
        while i < len(firstList) and j < len(secondList):
            # 情况1，A在B的左
            if secondList[j][0] > firstList[i][1]:
                #那A和B就不想交，直接过
                i+=1
            elif secondList[j][1] < firstList[i][0]:
                j+=1
            elif firstList[i][0] <= secondList[j][0] and secondList[j][1] <= firstList[i][1]:
                #被包了
                ans.append([secondList[j][0],secondList[j][1]])
                j+=1
            elif secondList[j][0] <= firstList[i][0] and firstList[i][1] <= secondList[j][1]:
                ans.append([firstList[i][0],firstList[i][1]])
                i+=1
            elif secondList[j][0] >= firstList[i][0] and secondList[j][0] <= firstList[i][1]:
                ans.append([secondList[j][0],firstList[i][1]])
                i+=1
            elif firstList[i][0] >= secondList[j][0] and firstList[i][0] <= secondList[j][1]:
                ans.append([firstList[i][0],secondList[j][1]])
                j+=1


        return ans


print(Solution().intervalIntersection([[5,6]],[[5,10]]))