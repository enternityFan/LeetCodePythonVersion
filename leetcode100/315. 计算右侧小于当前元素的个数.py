#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：315. 计算右侧小于当前元素的个数.py
@Author ：HuntingGame
@Date ：2023-02-09 14:56 
C'est la vie!!! enjoy ur day :D
'''
from typing import List

class Node:
    def __init__(self,v,i):
        self.value = v
        self.index = i

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ans = []
        if not nums:
            return ans
        for i in range(len(nums)):
            ans.append(0)
            if len(nums) < 2:
                return ans
        arr = [None] * len(nums)
        for i in range(len(nums)):
            arr[i] = Node(nums[i],i)
        self.process(arr,0,len(arr)-1,ans)
        return ans

    def process(self,arr,l,r,ans):
        if l == r:
            return

        mid = l + ((r - l) >> 1)
        self.process(arr,l,mid,ans)
        self.process(arr,mid+1,r,ans)
        self.merge(arr,l,mid,r,ans)

    def merge(self,arr,l,m,r,ans):
        """
        如果出现两个数相等，那就拷贝右边的。
        :param arr:
        :param l:
        :param m:
        :param r:
        :param ans:
        :return:
        """
        help = [None] * (r - l  + 1)
        i = len(help) - 1
        p1 = m#左组最右的位置
        p2 = r#右组最右的位置
        while p1 >=l and p2 >= m + 1:
            if arr[p1].value > arr[p2].value:
                ans[arr[p1].index] = ans[arr[p1].index] + p2 - m
            if arr[p1].value > arr[p2].value:
                help[i] = arr[p1]
                i-=1
                p1-=1
            else:
                help[i] = arr[p2]
                i-=1
                p2-=1


        while p1 >=l:
            help[i] = arr[p1]
            i-=1
            p1-=1
        while p2 >=m +1:
            help[i] = arr[p2]
            i-=1
            p2-=1
        for i in range(len(help)):
            arr[l + i] = help[i]

print(Solution().countSmaller([5,2,6,1]))