# @Time : 2022-09-04 20:13
# @Author : Phalange
# @File : 剑指 Offer II 080. 含有 k 个元素的组合.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def __init__(self):
        self.ans = []
        self.tmp = []
    def combine(self, n: int, k: int) -> List[List[int]]:

        def process(idx):
            if len(self.tmp) == k:
                self.ans.append(self.tmp[:])
                return
            elif idx > n:
                return
            else:
                self.tmp.append(idx)
                process(idx+1)
                self.tmp.pop()
                process(idx+1)

        process(1)
        return self.ans



print(Solution().combine(4,2))


#TODO 下面代码超时，有空改进
"""
class Solution:
    def __init__(self):
        self.ans = []
        self.tmp = []
    def combine(self, n: int, k: int) -> List[List[int]]:

        self.process(list(range(1,n+1)),0,0,k)
        return self.ans


    def process(self,arr,idx,cur,k):
        if cur == k:
            if self.tmp not in self.ans:
                self.ans.append(self.tmp[:])
            return
        if idx == len(arr):
            return

        for i in range(idx,len(arr)):
            self.process(arr,idx+1,cur,k)
            self.tmp.append(arr[idx])
            self.process(arr,idx+1,cur+1,k)
            self.tmp.pop()
"""
