#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：选择排序.py
@Author ：HuntingGame
@Date ：2023-03-06 14:33 
C'est la vie!!! enjoy ur day :D
'''
import random

"""
从待排序序列中，找到关键字最小的元素；

如果最小元素不是待排序序列的第一个元素，将其和第一个元素互换；

从余下的 N - 1 个元素中，找出关键字最小的元素，重复(1)、(2)步，直到排序结束。
"""

def select_sort(arr):
    for i in range(len(arr)):
        min_idx = i #最小的元素索引
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        if i !=min_idx:
            arr[i],arr[min_idx] = arr[min_idx],arr[i]





arr = list(range(10))
random.shuffle(arr)
select_sort(arr)
print(arr)