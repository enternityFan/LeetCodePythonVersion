# @Time : 2022-08-10 21:10
# @Author : Phalange
# @File : 2120. 执行所有后缀指令.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        ans = []
        idx = 0
        while idx !=len(s):
            cur = startPos.copy()
            tmp = 0 # 表示可以执行几条指令
            for i in range(idx,len(s)):
                if s[i] == 'R':
                    cur[1]+=1
                elif s[i] == 'L':
                    cur[1]-=1
                elif s[i] == 'D':
                    cur[0]+=1
                elif s[i] == 'U':
                    cur[0]-=1
                if cur[0] <0 or cur[0] >=n or cur[1] < 0 or cur[1] >=n:
                    break
                else:
                    tmp +=1
            ans.append(tmp)
            idx +=1
        return ans

print(Solution().executeInstructions(3,[0,1],"RRDDLU"))