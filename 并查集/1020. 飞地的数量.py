# @Time : 2022-08-10 18:09
# @Author : Phalange
# @File : 1020. 飞地的数量.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def __init__(self):
        self.nodes = dict()
        self.parents = dict()
        self.sizeMap = dict()
        self.canFly = set() # 记录以key为头的可以飞出去的连通域
    def numEnclaves(self, grid: List[List[int]]) -> int:
        # 初始化并查集
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.nodes[i * n + j] = i * n + j
                    self.parents[i * n + j] = i * n + j
                    self.sizeMap[i * n + j] = 1
                    if i in [0,m-1] or j in [0,n-1]:
                        self.canFly.add(i*n+j)

        for i in range(m):
            for j in range(n):
                if i + 1 < m and grid[i + 1][j] == 1 and grid[i][j] == 1:
                    self.union(self.nodes[(i + 1) * n + j], self.nodes[i * n + j])

                if j + 1 < n and grid[i][j + 1] == 1 and grid[i][j] == 1:
                    self.union(self.nodes[i * n + j], self.nodes[i * n + j + 1])

        ans = 0
        for key,val in self.sizeMap.items():
            if key not in self.canFly:
                ans +=val

        return ans



    def isSameSet(self, a, b):
        if a not in self.nodes or b not in self.nodes:
            return
        return self.findFather(a) == self.findFather(b)

    def findFather(self, cur):
        path = []
        while cur != self.parents[cur]:
            path.append(cur)
            cur = self.parents[cur]

        while path:
            self.parents[path.pop()] = cur
        return cur

    def union(self, a, b):
        if a not in self.nodes or b not in self.nodes:
            return

        aHead = self.findFather(a)
        bHead = self.findFather(b)
        if aHead != bHead:
            aSize = self.sizeMap[aHead]
            bSize = self.sizeMap[bHead]
            big = aHead if aSize >= bSize else bHead
            small = bHead if aHead == big else aHead
            self.parents[small] = big
            self.sizeMap[big] = aSize + bSize
            self.sizeMap.pop(small)
            if small in self.canFly:
                self.canFly.remove(small)
                self.canFly.add(big)