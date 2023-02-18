#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：658. 找到 K 个最接近的元素.py
@Author ：HuntingGame
@Date ：2023-01-04 9:23 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        n = len(arr)
        # 首先判断x是不是比边界小或者大
        if x <= arr[0]:
            return arr[:k]
        if x >=arr[-1]:
            return arr[-k:]
        # 开始二分查找
        # 首先都减去x并求绝对值
        #myarr = []
        #for c in arr:
        #    myarr.append(abs(c-x))
        #ori_idx = list(range(n))
        #arr,myarr = zip(*sorted(zip(arr,myarr),key=lambda x:(x[1],x[0])))
        # 现在排好序了
        #print(list(arr))
        #print(myarr)
        arr.sort(key=lambda c:abs(c-x))
        return sorted(arr[:k])

print(Solution().findClosestElements([1,2,3,4,5],4,3))











