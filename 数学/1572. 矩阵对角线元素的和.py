# @Time : 2022-08-20 12:28
# @Author : Phalange
# @File : 1572. 矩阵对角线元素的和.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        if n == 1:
            return mat[0][0]
        ans = 0
        if n % 2 == 1:
            ans -=mat[n//2][n//2]

        for i in range(n):
            print(i,n-1-i)
            ans = ans + mat[i][i]+mat[i][n-1-i]

        return ans

print(Solution().diagonalSum([[7,3,1,9],[3,4,6,9],[6,9,6,6],[9,5,8,5]]))