#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：1079. 活字印刷.py
@Author ：HuntingGame
@Date ：2023-03-18 22:05 
C'est la vie!!! enjoy ur day :D
'''
import collections

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        ans = set()
        def helper(left,right):
            if left:
                ans.add(left)
            for i in range(len(right)):
                helper(left+right[i],right[:i]+right[i+1:])
        helper("",tiles)
        return len(ans)

print(Solution().numTilePossibilities("AAB"))