#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：4. 寻找两个正序数组的中位数.py
@Author ：HuntingGame
@Date ：2023-02-01 10:37 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        这个题的求解思路是找有序数组中第k大的数字，
        :param nums1:
        :param nums2:
        :return:
        """


        longs = nums1 if len(nums1) >= len(nums2) else nums2
        shorts = nums1 if len(nums1) < len(nums2) else nums2
        l = len(longs)
        s = len(shorts)
        if s == 0:
            if l %2==0:
                return (longs[l//2]+longs[l//2-1]) / 2
            else:
                return longs[l//2]



        kth = (l+s) // 2+1 if (l+s) %2 == 1 else (l+s) // 2 #第k的意思。
        ans = 0
        for i in range(2):
            kth +=i
            if i == 1 and (l+s) %2 ==1.0:
                return ans
            if kth <= s:
                #情况1，k小于等于短数组的长度,那就两个数组都拿一段，就在这里面
                ans+= self.getUpMedian(shorts,0,kth-1,longs,0,kth-1)
                continue

            if kth > l:
                #情况2，k是比长数组的长度长的，那就手动排除掉两个，如果在排除的过程中可以返回了，那就返回了，不然就是排除了嘛，那就getUpMedian里面找
                #比如arr1是[1...10],arr2是[1...17]找第15小的数，那么arr1是都有可能的，arr2中可以一定排除掉[1,2,3,4,16,17],然后再通过下面的判断再去掉两个。
                if shorts[kth-l - 1] >= longs[l-1]:

                    ans+= shorts[kth -l-1]
                    continue
                if longs[kth - s - 1] >= shorts[s - 1]:
                    ans+= longs[kth - s - 1]
                    continue
                ans+= self.getUpMedian(shorts,kth-l,s-1,longs,kth-s,l-1)
                continue
            #情况3，需要手动排除掉一个，这个其实就是落在第二段里面。
            # 比如arr1是[1...10],arr2是[1...17]找第23小的数,那么arr1中的[1,2,3,4,5]是一定能排除掉的。arr2中的[1...12]是都不可能的。
            if longs[kth - s - 1] >=shorts[s - 1]:
                ans+= longs[kth -s -1]
                continue
            ans+= self.getUpMedian(shorts,0,s-1,longs,kth-s,kth-1)
            continue
        return ans /2









    def getUpMedian(self,a1,s1,e1,a2,s2,e2):
        """
        s1到e1和s2到e2是一定等长的。
        :param a1:
        :param s1:
        :param e1:
        :param a2:
        :param s2:
        :param e2:
        :return:
        """
        mid1 = 0
        mid2 = 0

        while s1 < e1:
            mid1 = (s1 + e1) // 2
            mid2 = (s2 + e2) // 2
            if a1[mid1] == a2[mid2]:
                return a1[mid1]
            if (e1 - s1 + 1) & 1 == 1:
                # 奇数长度
                if a1[mid1] > a2[mid2]:
                    if a2[mid2] >=a1[mid1 - 1]:
                        return a2[mid2]
                    e1 = mid1 - 1
                    s2 = mid2 + 1
                else:# a1[mid1] < a2[mid2]
                    if a1[mid1] >= a2[mid2-1]:
                        return a1[mid1]
                    e2 = mid2 - 1
                    s1 = mid1 + 1


            else:
                if a1[mid1] > a2[mid2]:
                    e1 = mid1
                    s2 = mid2 + 1
                else:
                    e2 = mid2
                    s1 = mid1 + 1

        return min(a1[s1],a2[s2])

print(Solution().findMedianSortedArrays([3],[-2,-1]))