#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：378. 有序矩阵中第 K 小的元素.py
@Author ：HuntingGame
@Date ：2023-02-16 14:14 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        #1 5 9
        #10 11 13
        #12 13 15
        #
        #
        nums = []
        i = 0
        j = 0
        cnt = 1
        heapq.heappush(nums, (nums[i][j],i,j))

        while i <=len(matrix)-1 and j <=len(matrix[0]) - 1:
            if nums[i][j+1] >= nums[i+1][j]:
                heapq.heappop(nums)
                heapq.heappush(nums,(nums[i][j+1],i,j+1))

            else:
                heapq.heappush(nums,(nums[i+1][j],i+1,j))

            cnt +=1
            if cnt == k:
                break

        return matrix[i][j]

