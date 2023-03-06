#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：插入排序.py
@Author ：HuntingGame
@Date ：2023-03-06 14:18 
C'est la vie!!! enjoy ur day :D
'''

import random
"""
空间复杂度O(1)
当数据正序时，执行效率最好，每次插入都不用移动前面的元素，时间复杂度为O(N)。

当数据反序时，执行效率最差，每次插入都要前面的元素后移，时间复杂度为O(N^2)。


直接插入排序，每次将一个新数据插入到有序队列中的合适位置里。
"""

def insert_sort(arr):
    """
    时间复杂度O(N^2)，空间复杂度O(1)
    :param arr:
    :return:
    """
    for i in range(len(arr)):
        for j in range(i,-1,-1):
            if j-1 >=0 and arr[j] < arr[j-1]:
                arr[j],arr[j-1] = arr[j-1],arr[j]
            else:
                break
        print("第%d趟" % i,arr)











arr = list(range(10))
random.shuffle(arr)
insert_sort(arr)
print(arr)