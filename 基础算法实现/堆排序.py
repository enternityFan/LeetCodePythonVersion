#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：堆排序.py
@Author ：HuntingGame
@Date ：2023-03-06 14:43 
C'est la vie!!! enjoy ur day :D
'''


"""

堆是一棵顺序存储的完全二叉树。

其中每个结点的关键字都不大于其孩子结点的关键字，这样的堆称为小根堆。

其中每个结点的关键字都不小于其孩子结点的关键字，这样的堆称为大根堆。


（1）根据初始数组去构造初始堆（构建一个完全二叉树，保证所有的父结点都比它的孩子结点数值大）。

（2）每次交换第一个和最后一个元素，输出最后一个元素（最大值），然后把剩下元素重新调整为大根堆。


"""
import math
def buildMaxHeap(arr):
    for i in range(math.floor(len(arr)/2),-1,-1):
        #heapify(arr,i)
        pass

#TODO


