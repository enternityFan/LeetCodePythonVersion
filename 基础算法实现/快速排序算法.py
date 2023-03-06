#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：快速排序算法.py
@Author ：HuntingGame
@Date ：2023-03-06 13:58 
C'est la vie!!! enjoy ur day :D
'''
import random

"""
快排的基本思想是取一个元素p，一般是第一个元素，使元素p归位，
列表被p分成两部分，左边都比p小，右边都比p大
递归完成排序
"""

def partition(arr,left,right):
    tmp = arr[left]
    while left < right:
        while left<right and arr[right] >=tmp:
            right -=1
        arr[left] = arr[right] #跳出了上面的循环，说明arr[right]的位置没有tmp大
        while left<right and arr[left]<=tmp:
            left+=1
        arr[right] = arr[left]

    arr[left] = tmp
    return left


def quick_sort(arr,left,right):
    if left < right:
        mid = partition(arr,left,right)
        quick_sort(arr,left,mid-1)
        quick_sort(arr,mid+1,right)


arr = list(range(10))
random.shuffle(arr)
quick_sort(arr,0,len(arr)-1)
print(arr)