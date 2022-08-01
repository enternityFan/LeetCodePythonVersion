# @Time : 2022-08-01 11:17
# @Author : Phalange
# @File : 1046. 最后一块石头的重量.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # 通过对石头取反，来得到大顶堆吧
        stones = [-each for each in stones]
        heapq.heapify(stones)
        while len(stones) >1:
            a,b = heapq.heappop(stones),heapq.heappop(stones)
            if a != b:
                heapq.heappush(stones,a-b)
        if len(stones) == 0:
            return 0
        return -stones[0]



print(Solution().lastStoneWeight([2,7,4,1,8,1]))