#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/11/13 17:17
# @Author  : HuntingGame
# @FileName: 1647. 字符频次唯一的最小删除次数.py
# @Software: PyCharm
# C'est la vie. Enjoy ur day ! :D
import collections


class Solution:
    def minDeletions(self, s: str) -> int:
        cnts = collections.Counter(s)
        ans = 0
        queset = set(cnts.values())
        quelist = list(cnts.values())
        quelist.sort()
        print(quelist)
        print(queset)
        if len(quelist) == 1:
            return 0
        for i in range(1,len(quelist)):
            if quelist[i] == quelist[i-1]:
                for j in range(quelist[i]-1,-1,-1):
                    if j not in queset:
                        ans +=quelist[i] - j
                        quelist[i] = j
                        for k in range(i-1,-1,-1):
                            if quelist[k] > quelist[i]:
                                quelist[k],quelist[i] = quelist[i],quelist[k]
                                break
                        if j !=0:
                            queset.add(j)
                        break


        print(cnts)
        return ans

print(Solution().minDeletions("abcabc"))