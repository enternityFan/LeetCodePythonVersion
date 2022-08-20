# @Time : 2022-08-20 11:42
# @Author : Phalange
# @File : 841. 钥匙和房间.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        arr = [0] * n
        arr[0] = 1 #默认第0个门是开的

        def dfs(cur):
            arr[cur] =1
            for it in rooms[cur]:
                if arr[it]==0:
                    dfs(it)


        dfs(0)

        return True if sum(arr) == n else False

rooms = [[6,7,8],[5,4,9],[],[8],[4],[],[1,9,2,3],[7],[6,5],[2,3,1]]
print(Solution().canVisitAllRooms(rooms))