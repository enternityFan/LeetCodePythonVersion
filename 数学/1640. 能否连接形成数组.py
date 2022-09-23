#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePythonVersion 
@File ：1640. 能否连接形成数组.py
@Author ：HuntingGame
@Date ：2022/9/22 8:11 
C'est la vie!!! :)
'''
from typing import List


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        n = len(arr)
        i = 0
        previ = i
        while i <n:
            previ = i
            for each in pieces:
                if i < n and each[0] == arr[i]:
                    for e in each:
                        if e == arr[i]:

                            i +=1
                        else:
                            return False
            if i == previ:
                return False



        return True
arr = [3,4,8]
pieces = [[3],[5],[8]]
print(Solution().canFormArray(arr,pieces))