#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：295. 数据流的中位数.py
@Author ：HuntingGame
@Date ：2023-02-08 19:56 
C'est la vie!!! enjoy ur day :D
'''
class MedianFinder:

    def __init__(self):
        """
        一个大根堆，一个小根堆来做。
        这样就会保证，最小的n/2个数都在小根堆里，大的n/2个数都在大根堆里。
        logN级别的。
        如果大根堆的大小是小根堆大小+2，那么就把大根堆的堆顶弹出加入到小根堆里；
        如果大根堆的大小等于小根堆大小-2，那么就把小根堆的堆顶弹出加入到大根堆你。
        最后，找中位数其实，就是两个堆的大小一样，那就返回他俩顶部数据除于2
        如果不一样，那么谁的size大就返回谁的堆顶。
        """


    def addNum(self, num: int) -> None:
        #TODO
        pass


    def findMedian(self) -> float:
        pass


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()