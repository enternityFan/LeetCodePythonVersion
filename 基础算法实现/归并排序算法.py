#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：归并排序算法.py
@Author ：HuntingGame
@Date ：2023-03-06 14:06 
C'est la vie!!! enjoy ur day :D
'''
import random

def merge_sort1(arr):

    return process(arr,0,len(arr) - 1)


def process(arr,L,R):
    if L == R:
        return
    mid = L + ((R - L) >> 1)
    process(arr,L,mid)
    process(arr,mid + 1,R)
    merge(arr,L,mid,R)

def merge(arr,L,M,R):
    help = [0] * (R - L +1)
    i = 0
    p1 = L
    p2 = M + 1
    while p1 <=M and p2 <=R:
        if arr[p1] <= arr[p2]:
            help[i] = arr[p1]
            p1 +=1
        else:
            help[i] = arr[p2]
            p2+=1
        i+=1
    #可能p1越界，也可能p2越界.
    while p1 <=M:
        help[i] = arr[p1]
        i+=1
        p1+=1
    while p2 <=R:
        help[i] = arr[p2]
        i+=1
        p2+=1

    #拷贝回去
    for i in range(len(help)):
        arr[L+i] = help[i]


def merge_sort2(arr):
    """
    非递归版本的实现
    :param arr:
    :return:
    """

    n = len(arr)
    mergeSize = 1 #当前有序的左组长度
    while mergeSize<n:
        L = 0
        while L < n:
            M = L + mergeSize - 1
            if M >=n:
                break
            R = min(M+mergeSize,n-1)
            merge(arr,L,M,R)
            L = R + 1
        if mergeSize > n //2:
            break
        mergeSize <<=1

arr = list(range(10))
arr2 = list(range(20))
random.shuffle(arr)
random.shuffle(arr2)
merge_sort1(arr)
merge_sort2(arr2)


print(arr)
print(arr2)