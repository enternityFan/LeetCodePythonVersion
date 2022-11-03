#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/10/29 18:06
# @Author  : HuntingGame
# @FileName: 2244. 完成所有任务需要的最少轮数.py
# @Software: PyCharm
# C'est la vie. Enjoy ur day ! :D
import collections
from typing import List


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        mycnt = collections.Counter(tasks)
        ans = 0
        for key,val in mycnt.items():
            if val == 1:
                return -1
            elif val % 2!=0 and val % 3 !=0 and val % 2!=3 and val % 3 !=2 and val %3 !=1:
                return -1
            elif val % 3 == 0:
                ans +=val // 3

            elif val %3 == 2:
                ans +=val //3 + 1
            elif val %3 == 1:
                ans +=val //3 + 1
            elif val % 2 == 0:
                ans +=val // 2
            elif val %2 == 3:
                ans +=val // 2 + 1
        return ans
tasks = [66,66,63,61,63,63,64,66,66,65,66,65,61,67,68,66,62,67,61,64,66,60,69,66,65,68,63,60,67,62,68,60,66,64,60,60,60,62,66,64,63,65,60,69,63,68,68,69,68,61]
print(Solution().minimumRounds(tasks))