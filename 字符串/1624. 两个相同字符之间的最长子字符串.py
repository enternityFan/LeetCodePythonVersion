#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePythonVersion 
@File ：1624. 两个相同字符之间的最长子字符串.py
@Author ：HuntingGame
@Date ：2022/9/17 12:06 
C'est la vie!!! :)
'''
import collections


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        mydict = collections.defaultdict(list)
        ans = -1
        for i,c in enumerate(s):
            mydict[c].append(i)
            if len(mydict[c]) >= 2:
                ans = max(ans,mydict[c][-1] - mydict[c][0]-1)

        return ans

print(Solution().maxLengthBetweenEqualCharacters("mgntdygtxrvxjnwksqhxuxtrv"))