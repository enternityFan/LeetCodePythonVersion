#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePythonVersion 
@File ：60. 排列序列.py
@Author ：HuntingGame
@Date ：2022/9/21 12:59 
C'est la vie!!! :)
'''


class Solution:
    def __init__(self):
        self.ans = []
        self.tmp = []
        self.times = 0
    def getPermutation(self, n: int, k: int) -> str:

        def process(used):
            if self.times == k+1:
                return
            if len(self.tmp) == n:
                if self.times == k-1:
                    self.ans.append("".join(self.tmp[:]))
                #print(self.tmp)
                self.times +=1

                return

            for i in range(1,n+1):
                if self.times == k+1:
                    return
                if i in used:
                    continue

                self.tmp.append(str(i))
                used.add(i)
                process(used)
                self.tmp.pop()
                used.remove(i)


        process(set())
        return self.ans[0]

print(Solution().getPermutation(9,138270))
