# @Time : 2022-08-20 20:40
# @Author : Phalange
# @File : 739. 每日温度.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                ans[prev_index] = i-prev_index
            stack.append(i)

        return ans

print(Solution().dailyTemperatures([73,73,73,71,69,72,76,73]))