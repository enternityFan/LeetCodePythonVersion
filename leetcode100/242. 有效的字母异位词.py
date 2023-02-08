#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：242. 有效的字母异位词.py
@Author ：HuntingGame
@Date ：2023-02-08 13:19 
C'est la vie!!! enjoy ur day :D
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1 = len(s)
        l2 = len(t)
        if l1 !=l2:
            return False

        arr = [0] * 26
        for c in s:
            arr[ord(c) - ord('a')] +=1

        for c in t:
            arr[ord(c) - ord('a')] -=1
            if arr[ord(c) - ord('a')] <0:
                return False
        return True