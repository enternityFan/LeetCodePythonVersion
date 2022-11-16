#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：1710. 卡车上的最大单元数.py
@Author ：HuntingGame
@Date ：2022-11-15 9:28 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:x[1],reverse=True)
        ans = 0
        flag = 0
        for i in range(len(boxTypes)):
            if flag + boxTypes[i][0] < truckSize:
                ans +=boxTypes[i][0] * boxTypes[i][1]
                flag +=boxTypes[i][0]
            elif flag+boxTypes[i][0] == truckSize:
                ans +=boxTypes[i][0] * boxTypes[i][1]
                flag+=boxTypes[i][0]
                break
            else:
                ans +=(truckSize-flag) * boxTypes[i][1]
                break

        return ans
