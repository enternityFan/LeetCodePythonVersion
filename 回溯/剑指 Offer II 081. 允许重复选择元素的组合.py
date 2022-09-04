# @Time : 2022-09-04 20:40
# @Author : Phalange
# @File : 剑指 Offer II 081. 允许重复选择元素的组合.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def __init__(self):
        self.ans = []
        self.tmp = []

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.process(candidates, 0, target)
        return self.ans

    def process(self, arr, idx, target):
        if sum(self.tmp) == target:
            if self.tmp not in self.ans:
                self.ans.append(self.tmp[:])
            return 2
        elif sum(self.tmp) > target:
            return 1

        elif idx == len(arr):
            return 0

        self.tmp.append(arr[idx])
        tmp = self.process(arr, idx, target)
        if tmp == None or tmp ==0:
            tmp = self.process(arr, idx + 1, target)
        self.tmp.pop()
        if tmp == None or tmp == 0:
            self.process(arr, idx + 1, target)


candidates = [2, 3, 5]
target = 8
print(Solution().combinationSum(candidates, target))
