# @Time : 2022-10-14 12:30
# @Author : Phalange
# @File : 1314. 矩阵区域和.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List



class Solution2:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        ans = [[0] * n for _ in range(m)]
        for i in range(m):

            for j in range(n):

                tmp = 0
                li = i-k if i>=k else 0
                lj = j-k if j>=k else 0
                ri = i+k if i+k <m else m-1
                rj = j+k if j+k <n else n-1
                for ii in range(li,ri+1):
                    for jj in range(lj,rj+1):
                        tmp+=mat[ii][jj]
                ans[i][j] = tmp
        return ans