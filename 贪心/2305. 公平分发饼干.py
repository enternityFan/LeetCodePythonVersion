#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/10/21 16:38
# @Author  : HuntingGame
# @FileName: 2305. 公平分发饼干.py
# @Software: PyCharm
# C'est la vie. Enjoy ur day ! :D
import math
from typing import List

class Solution2:
    def __init__(self):
        self.ans = []

    def distributeCookies(self, cookies: List[int], k: int) -> int:
        tmp = [[0] * k for _ in range(len(cookies))]


class Solution:
    def __init__(self):
        self.ans = 10000000

    def distributeCookies(self, cookies: List[int], k: int) -> int:
        """
        回溯的做法超时
        添加剪枝操作：1.排序；2.如果剩余的饼干包不够还没有拿到饼干的小朋友分了，直接返回。
        3，如果当前状态下某位小朋友的饼干数量比当前的答案还多，显然继续回溯下去也无法成为最优答案，直接返回。
        4.第一个零食包不管给哪个小朋友，所开启的回溯树都一样，所以首个饼干包只要给第一个小朋友就行了，这样的回溯树只有一个根节点（一个回溯树），否则有k个回溯树。
        """
        tmp = [0] * k
        # ans = math.inf
        cookies.sort(reverse=True)

        def process(idx):

            if idx == len(cookies):
                self.ans = min(self.ans, max(tmp))

                return

            # 判断是否不够分
            zcnt = 0
            for i in tmp:
                if i == 0: zcnt += 1
            if zcnt > len(cookies) - idx:
                return  # 这个方案不行
            for i in range(k):
                if tmp[i] > self.ans:
                    return  # 这个方案不行
            for i in range(k):
                tmp[i] += cookies[idx]
                process(idx + 1)
                tmp[i] -= cookies[idx]

        process(0)
        return self.ans

cookies = [8,15,10,20,8]
k = 2
print(Solution().distributeCookies(cookies,k))
