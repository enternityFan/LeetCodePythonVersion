#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/10/22 21:13
# @Author  : HuntingGame
# @FileName: 1010. 总持续时间可被 60 整除的歌曲.py
# @Software: PyCharm
# C'est la vie. Enjoy ur day ! :D
from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        mod = [0] * 60
        for i in range(len(time)):
            mod[time[i]%60] +=1

        ans =mod[0]*(mod[0]-1)//2
        for i in range(1,30):
            ans +=(mod[i]*mod[60-i])
        ans +=(mod[30] * (mod[30]-1)//2)
        return ans
print(Solution().numPairsDivisibleBy60([15,63,451,213,37,209,343,319]))