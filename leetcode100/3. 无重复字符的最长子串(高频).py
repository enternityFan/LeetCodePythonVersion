#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：3. 无重复字符的最长子串(高频).py
@Author ：HuntingGame
@Date ：2023-02-01 10:15 
C'est la vie!!! enjoy ur day :D
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        求出来所有i位置出来的可能，然后求一个max
        通过在遍历的过程中更新一个map来实现。
        第i位置的可能只跟i位置和i-1位置的可能有关。
        :param s:
        :return:
        """
        if s == "":
            return 0
        mymap = [-1]*256# 这里用数组，因为数组比哈希表更快。256表示ASCII码。
        pre = -1 # i-1结尾的位置，往前推不动的位置是谁。
        ans = 0
        for i in range(len(s)):
            #i位置结尾往左推，推不动的是谁= 最近的上一个推不动的和理我推不动的离我最近的是谁。
            #相当于此时pre从i-1位置的信息变为了i位置结尾的信息。
            pre = max(pre,mymap[ord(s[i])])
            cur = i - pre
            ans = max(ans,cur)
            mymap[ord(s[i])] = i
        return ans