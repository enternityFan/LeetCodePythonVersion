# @Time : 2022-08-20 22:30
# @Author : Phalange
# @File : 6156. 得到 K 个黑块的最少涂色次数.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D


class Solution2:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        self.ans = 10000
        def process(i,cnt,times):
            if cnt == k:
                self.ans = min(self.ans,times)
                return
            if i == len(blocks):
                return

            if blocks[i] == "B":
                process(i+1,cnt+1,times)
            else:
                process(i+1,cnt+1,times+1)
                process(i+1,0,times)

        process(0,0,0)
        return self.ans

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        self.ans = 10000
        arr = [0] * n
        for i in range(n):
            if blocks[i] == "B":
                arr[i][0] +=1
                arr[i][1] = arr[i-1][1]
            else:
                pass





        def process(i,cnt,times):
            if cnt == k:
                self.ans = min(self.ans,times)
                return
            if i == len(blocks):
                return

            if blocks[i] == "B":
                process(i+1,cnt+1,times)
            else:
                process(i+1,cnt+1,times+1)
                process(i+1,0,times)

        process(0,0,0)
        return self.ans

print(Solution().minimumRecolors("BWWWBB",6))