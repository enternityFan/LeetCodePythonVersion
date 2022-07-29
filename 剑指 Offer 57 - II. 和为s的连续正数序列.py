# @Time : 2022-07-29 20:16
# @Author : Phalange
# @File : 剑指 Offer 57 - II. 和为s的连续正数序列.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D.
from typing import List


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        res = []

        for i in range(1,target):

            arr = []
            count = 0
            for j in range(i,target):
                count += j
                arr.append(j)
                if count > target:
                    break
                elif count == target:
                    res.append(arr)
                    break

        return res



