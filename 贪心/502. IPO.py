# @Time : 2022-08-09 10:44
# @Author : Phalange
# @File : 502. IPO.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import collections
import heapq
from typing import List

class Program:
    def __init__(self,p,c):
        self.p = p
        self.c = c


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        if w >=max(capital):
            return w + sum(heapq.nlargest(k,profits))
        n = len(profits)
        curr = 0
        arr = [(capital[i],profits[i]) for i in range(n)]
        arr.sort(key=lambda x:x[0])

        pq = []
        for _ in range(k):
            while curr < n and arr[curr][0] <=w:
                heapq.heappush(pq,-arr[curr][1])
                curr +=1

            if pq:
                w -=heapq.heappop(pq)
            else:
                break
        return w


k = 2
w = 0
profits = [1,2,3]
capital = [0,1,1]
print(Solution().findMaximizedCapital(k,w,profits,capital))