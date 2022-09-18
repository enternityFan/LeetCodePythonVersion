# @Time : 2022-09-18 12:26
# @Author : Phalange
# @File : 1605. 给定行和列的和求可行矩阵.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List
import random

class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        nrow = len(rowSum)
        ncol = len(colSum)
        ans = [[0]*ncol for _ in range(nrow)]
        for i in range(nrow):
            for j in range(ncol):
                ans[i][j] = rowSum[i] if rowSum[i] < colSum[j] else colSum[j]
                rowSum[i] -=ans[i][j]
                colSum[j] -=ans[i][j]

        return ans