# @Time : 2022-10-17 13:30
# @Author : Phalange
# @File : 2225. 找出输掉零场或一场比赛的玩家.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import collections
from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        ans = [[],[]]
        winers = collections.defaultdict(int)
        losers = collections.defaultdict(int)
        for i in range(len(matches)):
            winers[matches[i][0]] +=1
            losers[matches[i][1]] +=1

        for key,val in winers.items():
            if key not in losers:
                ans[0].append(key)
        for key,val in losers.items():
            if val == 1:
                ans[1].append(key)
        ans[0].sort()
        ans[1].sort()
        return ans

