# @Time : 2022-08-10 18:06
# @Author : Phalange
# @File : 200. 岛屿数量.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def __init__(self):
        self.nodes = dict()
        self.parents = dict()
        self.sizeMap = dict()
    def numIslands(self, grid: List[List[str]]) -> int:
        # 初始化并查集
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.nodes[i*n+j] = i*n+j
                    self.parents[i*n+j] = i*n+j
                    self.sizeMap[i*n+j] = 1

        for i in range(m):
            for j in range(n):
                if i+1 < m and grid[i+1][j] == '1' and grid[i][j] == '1':
                    self.union(self.nodes[(i+1)*n + j],self.nodes[i*n+j])

                if j+1 < n and grid[i][j+1] == '1' and grid[i][j] =='1' :
                    self.union(self.nodes[i*n + j],self.nodes[i*n+j+1])
        if self.sizeMap == {}:
            return 0
        return len(self.sizeMap)


    def isSameSet(self,a,b):
        if a not in self.nodes or b not in self.nodes:
            return
        return self.findFather(a) == self.findFather(b)

    def findFather(self,cur):
        path = []
        while cur !=self.parents[cur]:
            path.append(cur)
            cur = self.parents[cur]

        while path:
            self.parents[path.pop()] = cur
        return cur



    def union(self,a,b):
        if a not in self.nodes or b not in self.nodes:
            return

        aHead = self.findFather(a)
        bHead = self.findFather(b)
        if aHead != bHead:
            aSize = self.sizeMap[aHead]
            bSize = self.sizeMap[bHead]
            big = aHead if aSize >=bSize else bHead
            small = bHead if aHead == big else aHead
            self.parents[small] = big
            self.sizeMap[big] = aSize + bSize
            self.sizeMap.pop(small)