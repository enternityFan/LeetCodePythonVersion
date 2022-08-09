# @Time : 2022-08-09 16:20
# @Author : Phalange
# @File : LCP 07. 传递信息.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def __init__(self):
        self.tmp = []
        self.ans = []
        self.times = 0
        self.mymap = None
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        def dfs(x:int,time:int):
            """
            k 为当前是第几轮
            :param x:
            :param k:
            :return:
            """
            if time == k:
                if x == n - 1:
                    self.ans.append(self.tmp[:])
                    self.times +=1
                return

            for y in self.mymap[x]:
                self.tmp.append(y)
                dfs(y,time+1)
                self.tmp.pop()


        # 首先制作map
        self.mymap = [[] for i in range(n)]
        for each in relation:
            self.mymap[each[0]].append(each[1])
        self.tmp.append(0)
        dfs(0,0)
        return self.times




n = 3
relation = [[0,1],[0,2],[2,1],[1,2],[1,0],[2,0]]
k = 5

print(Solution().numWays(n,relation,k))