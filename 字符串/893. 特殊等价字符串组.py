#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：893. 特殊等价字符串组.py
@Author ：HuntingGame
@Date ：2022-11-14 10:17 
C'est la vie!!! enjoy ur day :D
'''
import collections
from typing import List


class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:

        flag = [0] * len(words)
        ans = 0
        mydict = collections.defaultdict(int)
        for i in range(len(words)):

            even = ""
            odd = ""
            for c in range(len(words[i])):
                if c % 2 == 0:
                    even +=words[i][c]
                else:
                    odd +=words[i][c]
            even = sorted(even)
            odd = sorted(odd)
            mydict["".join(even) + "$" +"".join(odd)] +=1

        return len(mydict.keys())


words = ["abcd","cdab","cbad","xyzz","zzxy","zzyx"]
print(Solution().numSpecialEquivGroups(words))