# @Time : 2022-10-14 9:30
# @Author : Phalange
# @File : 1079. 活字印刷.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D



class Solution:

    def __init__(self):
        self.ans = []
        self.tmp = []
    def numTilePossibilities(self, tiles: str) -> int:
        tiles = [i for i in tiles]

        def process(idx):
            if idx == len(tiles):

                self.ans.append(self.tmp[:])
                #self.tmp = []
                return
            used = [0] * 26
            for i in range(idx,len(tiles)):

                if used[ord(tiles[i]) - ord('A')] == 0:
                    used[ord(tiles[i])-ord('A')] = 1
                    self.tmp.append(tiles[idx])
                    self.tmp[i], self.tmp[idx] = self.tmp[idx], self.tmp[i]
                    process(idx + 1)
                    self.tmp[i], self.tmp[idx] = self.tmp[idx], self.tmp[i]
                    self.tmp.pop()

        process(0)
        return self.ans

print(Solution().numTilePossibilities("AAB"))

