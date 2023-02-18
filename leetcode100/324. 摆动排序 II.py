#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：324. 摆动排序 II.py
@Author ：HuntingGame
@Date ：2023-02-09 19:07 
C'est la vie!!! enjoy ur day :D
'''
import math
from random import random
from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        额外空间复杂度O(1),时间复杂度O(N)做到这个难度，就是超难的。这个代码就是的。
        思路：首先找到中位数，小于中位数的放左，等于放中间，大于放右边。
        那么找中位数的方法，就用bfprt算法，不过这里不用！这里用的类似快排的方式，为了O(1)的空间复杂度。
        快排的时间复杂度O(NlogN),不过这里的其实是只进一个递归，所以可以O（N）
        """
        if len(nums) < 2:
            return
        N = len(nums)
        median = self.findIndexNum(nums,0,N-1,N//2)

        #这个使用其实，已经因为findIndexNum给partition好了。
        if N & 1 == 0:
            """
            偶数长度，比如说[3 2 1 4| 4 7 6 8],其实是[L1,L2,L3,L4|R1,R2,R3,R4]
            那么下面的操作就是[L1 R1 L2 R2 L3 R3 L4 R4]==>[3 4 2 7 1 6 4 8]符合题意。
            """
            self.shuffle(nums,0,N-1)
            self.reverse(nums,0,N-1)
        else:

            """
            奇数长度[3|1 2 4|4 6 5],其实就是[0|L1 L2 L3|R1 R2 R3]
            直接调整为[0|R1 L1 R2 L2 R3 L3]===>[3,4,6,2,5,4] 

            """
            self.shuffle(nums,1,N-1)

    def findIndexNum(self,arr,L,R,index):
        """
        arr在L。。。R上找index位置的数
        :param arr:
        :param L:
        :param R:
        :param index:
        :return:
        """
        pivot = 0
        range = []
        while L < R:
            pivot = arr[L + int(random.random()*(R-L+1))]
            range = self.partition(arr,L,R,pivot)
            if index >=range[0] and index <= range[1]:
                return arr[index]
            elif index < range[0]:
                R = range[0] - 1
            else:
                L = range[1] + 1
        return arr[L]


    def partition(self,arr,L,R,pivot):
        """

        返回一个数组[等于区域的左边界，等于区域的右边界]
        :param arr:
        :param L:
        :param R:
        :return:
        """
        less = L - 1
        more = R + 1
        cur = L
        while cur < more:
            if arr[cur] < pivot:
                less+=1
                arr[less],arr[cur]=arr[cur],arr[less]
                cur+=1
            elif arr[cur] > pivot:
                more -=1
                arr[cur],arr[more] = arr[more],arr[cur]

            else:
                cur +=1
        return [less + 1,more -1]

    def shuffle(self,nums,l,r):


        while r - l + 1 >0:
            lenAndOne = l - l + 2
            bloom = 3
            k = 1
            while bloom <= lenAndOne // 3:
                bloom *=3
                k +=1
                self.cycles(nums,l-1,bloom,k)
                l = l + bloom - 1

    def cycles(self,nums,base,bloom,k):
        #TODO 71leetcode（23）课的1h43min22s;
        #不想写了。。
        pass



