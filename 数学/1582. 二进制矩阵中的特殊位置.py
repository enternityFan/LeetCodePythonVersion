# @Time : 2022-09-04 18:43
# @Author : Phalange
# @File : 1582. 二进制矩阵中的特殊位置.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        ans = 0
        r = len(mat)
        c = len(mat[0])
        for i in range(r):
            for j in range(c):
                if mat[i][j] == 1 and sum(mat[i]) == 1:
                    # 判断一下列是不是满足要求
                    tmp = 0
                    for k in range(r):
                        tmp += mat[k][j]

                    if tmp == 1:
                        ans += 1
        return ans


mat = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
print(Solution().numSpecial(mat))
