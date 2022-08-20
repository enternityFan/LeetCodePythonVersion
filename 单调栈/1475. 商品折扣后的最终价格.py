# @Time : 2022-08-20 21:28
# @Author : Phalange
# @File : 1475. 商品折扣后的最终价格.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        ans = [0] *n
        stack = []
        for i in range(n):
            while stack and prices[stack[-1]] >= prices[i]:
                idx = stack.pop()
                ans[idx] = prices[idx] -  prices[i]
            stack.append(i)

        while stack:
            idx = stack.pop()
            ans[idx] = prices[idx]

        return ans

print(Solution().finalPrices([8,4,6,2,3]))