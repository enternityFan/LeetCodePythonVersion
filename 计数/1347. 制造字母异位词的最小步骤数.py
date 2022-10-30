#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/10/29 15:40
# @Author  : HuntingGame
# @FileName: 1347. 制造字母异位词的最小步骤数.py
# @Software: PyCharm
# C'est la vie. Enjoy ur day ! :D
import collections


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        scnter = collections.Counter(s)
        tcnter = collections.Counter(t)
        if scnter == tcnter:
            return 0
        ans = 0
        for key,val in scnter.items():
            if key in tcnter:
                if val - tcnter[key] >=0:
                    ans += val - tcnter[key]


            else:
                ans +=val

        return ans

s = "leetcode"
t = "practice"
print(Solution().minSteps(s,t))