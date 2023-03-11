#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：面试题 17.05. 字母与数字.py
@Author ：HuntingGame
@Date ：2023-03-11 18:43 
C'est la vie!!! enjoy ur day :D
'''
import collections
from typing import List


class Solution:
    def findLongestSubarray(self, array: List[str]) -> List[str]:

        mydict1 = collections.defaultdict(int)#i: num_nums存放以i为结尾时数组的num的数目
        mydict2 = collections.defaultdict(int)#i: num_nums存放以i为结尾时数组的char的数目`
        mydict3 = collections.defaultdict(list) #num_nums:[idx]
        mydict4 = collections.defaultdict(list) #num_chars:[idx]
        num_nums = 0
        num_chars = 0

        ans = -1 #当前的最大长度
        L = 0
        R = 0
        for i in range(len(array)):
            if (array[i] >="a" and array[i] <="z") or (array[i] >="A" and array[i] <="Z"):
                num_chars +=1
            else:
                num_nums +=1
            mydict1[i] = num_nums
            mydict2[i] = num_chars
            mydict3[num_nums].append(i)
            mydict4[num_chars].append(i)
            if mydict1[i] == mydict2[i] and 2 * mydict1[i] > ans:
                ans = 2 * mydict1[i]
                L = 0
                R = i
            elif mydict1[i] > mydict2[i] and (mydict1[i] - mydict2[i]) in mydict3 :
                if i -  mydict3[mydict1[i] - mydict2[i]][0] > ans:
                    ans = i - mydict3[mydict1[i] - mydict2[i]][0]
                    L = mydict3[mydict1[i] - mydict2[i]][0]+1
                    R = i
            elif mydict2[i] > mydict1[i] and (mydict2[i] - mydict1[i]) in mydict4:
                if i -  mydict4[mydict2[i] - mydict1[i]][0] > ans:
                    ans = i - mydict4[mydict2[i] - mydict1[i]][0]
                    L = mydict4[mydict2[i] - mydict1[i]][0]+1
                    R = i

        if ans <= 0:
            return []
        return array[L:R+1]
a = ["42","10","O","t","y","p","g","B","96","H","5","v","P","52","25","96","b","L","Y","z","d","52","3","v","71","J","A","0","v","51","E","k","H","96","21","W","59","I","V","s","59","w","X","33","29","H","32","51","f","i","58","56","66","90","F","10","93","53","85","28","78","d","67","81","T","K","S","l","L","Z","j","5","R","b","44","R","h","B","30","63","z","75","60","m","61","a","5","S","Z","D","2","A","W","k","84","44","96","96","y","M"]

print(Solution().findLongestSubarray(a))
