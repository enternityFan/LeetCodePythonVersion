# @Time : 2022-08-11 21:27
# @Author : Phalange
# @File : 682. 棒球比赛.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        ans = []
        n = len(ops)
        for i in range(n):
            if ops[i] == "C":
                ans.pop()
            elif ops[i] == "D":
                ans.append(ans[-1]*2)
            elif ops[i] == "+":
                ans.append(ans[-1] + ans[-2])
            else:
                ans.append(int(ops[i]))
        return sum(ans)

print(Solution().calPoints(["5","2","C","D","+"]))