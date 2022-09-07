# @Time : 2022-09-07 20:45
# @Author : Phalange
# @File : 1583. 统计不开心的朋友.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List

#TODO
class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        ans = set()
        mat = []
        for i in range(len(preferences)):
            tmp = [-1] * (len(preferences))
            for j in range(len(preferences) - 1):
                tmp[preferences[i][j]] = len(preferences) - j - 1

            mat.append(tmp)

        for i in range(n // 2):
            for j in range( n // 2):
                if i == j :
                    continue
                if mat[pairs[i][0]][pairs[j][0]] > mat[pairs[i][0]][pairs[i][1]] and mat[pairs[j][0]][pairs[i][0]] > \
                        mat[pairs[j][0]][pairs[j][1]]:
                    ans.add(pairs[i][0])
                if mat[pairs[i][1]][pairs[j][1]] > mat[pairs[i][1]][pairs[i][0]] and mat[pairs[j][1]][pairs[i][1]] > \
                        mat[pairs[j][1]][pairs[j][0]]:
                    ans.add(pairs[i][1])

        return len(ans)


n = 4
preferences = [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]]
pairs = [[0, 1], [2, 3]]

print(Solution().unhappyFriends(n, preferences, pairs))
