#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：139. 单词拆分.py
@Author ：HuntingGame
@Date ：2023-02-06 10:21 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Node:
    def __init__(self):
        self.end = False  # 表示自己是不是某个节点的结束
        self.nexts = [None] * 26  # 往下走的26条路


class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 建立字典树
        root = Node()
        # print(root)
        for each in wordDict:
            node = root
            idx = 0
            for i in range(len(each)):
                idx = ord(each[i]) - ord('a')
                if node.nexts[idx] is None:
                    node.nexts[idx] = Node()

                node = node.nexts[idx]
            node.end = True

        # 下面的代码是改为DP的
        N = len(s)
        dp = [0] * (N + 1)
        dp[N] = 1
        # 从后往前推的，根据process能看出来。
        for idx in range(N - 1, -1, -1):
            cur = root
            print(s[idx])
            for end in range(idx, len(s)):
                # s[idx...end]
                #print(ord(s[end]))
                cur = cur.nexts[ord(s[end]) - ord('a')]
                if cur == None:
                    break  # 后面没路了，那就不用再试了，肯定这个前缀弄出来的后缀是不行的。
                if cur.end:
                    dp[idx] += dp[end + 1]

        return dp[0] != 0

    def wordBreak2(self, s: str, wordDict: List[str]) -> bool:
        # return self.process(s,0,wordDict) == 0 #如果这样的话，那就是这个力扣题的答案了
        # 下面的代码超时。
        return self.process(s, 0, wordDict)

    def wordBreak3(self, s: str, wordDict: List[str]) -> bool:
        """
        N^3的解法,两个for循环，还有一个判断是否在wordDict的事。
        这个时候可以用前缀树来优化掉，变为N^2,看wordBreak的代码。
        :param s:

        :param wordDict:
        :return:
        """
        # 下面的代码是改为DP的
        N = len(s)
        dp = [0] * (N + 1)
        dp[N] = 1
        # 从后往前推的，根据process能看出来。
        for idx in range(N - 1, -1, -1):
            ways = 0
            for end in range(len(s)):
                # s[idx...end]
                pre = s[idx:end + 1]
                if pre in wordDict:
                    ways += dp[end + 1]

        return dp[0] != 0

    def process(self, s, idx, wordDict):
        """

        [0...idx-1]这一段已经分解过了，不用再操心了
        [idx....]能够被分解的方法数，返回
        :param s:
        :param idx:
        :param wordDict:
        :return:
        """
        if idx == len(s):
            return 1

        # 枚举所有能不能做前缀
        ways = 0
        for end in range(len(s)):
            # s[idx...end]
            pre = s[idx:end + 1]
            if pre in wordDict:
                ways += self.process(s, end + 1, wordDict)

        return ways


print(Solution().wordBreak("leetcode", ["leet", "code"]))
