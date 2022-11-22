#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：354. 俄罗斯套娃信封问题.py
@Author ：HuntingGame
@Date ：2022-11-22 9:11 
C'est la vie!!! enjoy ur day :D
'''
from typing import List
import bisect

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:

        envelopes.sort(key=lambda x:(x[0],-x[1]))

        dp = [0]
        dp = [envelopes[0][1]]
        for i in range(1,len(envelopes)):
            j = bisect.bisect_left(dp,envelopes[i][1])
            if j < len(dp):
                dp[j] = envelopes[i][1]
            else:
                dp.append(envelopes[i][1])

        return len(dp)





a = [[5,4],[6,4],[6,7],[2,3]]
print(Solution().maxEnvelopes(a))

