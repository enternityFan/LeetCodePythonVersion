#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：1442. 形成两个异或相等数组的三元组数目.py
@Author ：HuntingGame
@Date ：2023-03-12 9:12 
C'est la vie!!! enjoy ur day :D
'''
from typing import List
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        """
        a==b其实就是si ^ sj = sj ^ sk+1  ----> si = sk+1
        :param arr:
        :return:
        """
        ans = 0
        s = [0]
        for val in arr:
            s.append(s[-1] ^ val)

        for i in range(len(arr)):
            for k in range(i+1,len(arr)):
                if s[i] == s[k+1]:
                    ans += k-i
        return ans

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        """
        方法1，三重循环
        :param arr:
        :return:
        """
        mydict = {}
        tmp = 0
        ans = 0
        for i in range(len(arr)):
            mydict[i] = tmp
            tmp ^=arr[i]
        for k in range(len(arr)):
            for j in range(k+1):
                for i in range(j):
                    a = mydict[i] ^ mydict[j]
                    b = mydict[j] ^ mydict[k] ^ arr[k]
                    if a == b:
                        ans +=1

        return ans

print(Solution().countTriplets([2,3,1,6,7]))





