# @Time : 2022-08-20 20:25
# @Author : Phalange
# @File : 剑指 Offer II 038. 每日温度.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 单调栈的一个典型问题
        n = len(temperatures)
        ans = [0]*n
        stack = []
        for i in range(n):
            # 底-》顶，是从大到小的
            while stack!=[] and temperatures[stack[-1][0]] < temperatures[i]:
                popIs = stack.pop()
                # 取位于下面位置的列表中，最晚加入的那个
                for each in popIs:
                    ans[each] = i-each

            #相等的，比你小的
            if stack != [] and temperatures[stack[-1][0]] == temperatures[i]:
                stack[-1].append(i)
            else:
                stack.append([i])

        # 最后再处理栈中还有没有处理的那些元素
        while stack:
            popIs = stack.pop()
            for each in popIs:
                ans[each] = 0

        return ans



print(Solution().dailyTemperatures([73,73,73,71,69,72,76,73]))