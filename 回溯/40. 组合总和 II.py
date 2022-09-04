# @Time : 2022-09-04 21:26
# @Author : Phalange
# @File : 40. 组合总和 II.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def __init__(self):
        self.ans = []
        self.tmp = []

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.process(candidates, 0, target)
        return self.ans

    def process(self, arr, idx, target):
        if sum(self.tmp) == target:
            self.ans.append(self.tmp[:])
            return 2
        elif sum(self.tmp) > target:
            return 1

        elif idx == len(arr):
            return 0

        self.tmp.append(arr[idx])

        tmp = self.process(arr, idx + 1, target)

        self.tmp.pop()

        if tmp == None or tmp == 0:
            self.process(arr, idx + 1, target)

candidates = [10,1,2,7,6,1,5]
target = 8
print(Solution().combinationSum2(candidates,target))