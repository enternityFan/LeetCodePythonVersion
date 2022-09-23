# @Time : 2022-09-20 21:09
# @Author : Phalange
# @File : 128. 最长连续序列.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:

    def __init__(self):
        self.nodes = dict()
        self.parents = dict()
        self.sizeMap = dict()

    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        n = len(nums)
        for i in range(n):
            self.nodes[nums[i]] = nums[i]
            self.parents[nums[i]] = nums[i]
            self.sizeMap[nums[i]] = 1

        # 连通起来
        for i in range(n):
            if nums[i]-1 in self.nodes:
                self.union(nums[i]-1,nums[i])

        return max(list(self.sizeMap.values()))

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

print(Solution().longestConsecutive([1,3,2]))





