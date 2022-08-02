# @Time : 2022-08-01 22:00
# @Author : Phalange
# @File : 378. 有序矩阵中第 K 小的元素.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        aimrows = k // n


