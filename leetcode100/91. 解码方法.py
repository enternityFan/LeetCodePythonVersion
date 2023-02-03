#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：91. 解码方法.py
@Author ：HuntingGame
@Date ：2023-02-03 18:57 
C'est la vie!!! enjoy ur day :D
'''
class Solution:
    def numDecodings(self, s: str) -> int:
        """
        从左往右的尝试模型
        :param s:
        :return:
        """
        if len(s) == 0:
            return 0
        N = len(s)
        dp = [0] * (N+1)
        dp[N] = 1
        for i in range(N-1,-1,-1):
            if s[i] != '0':
                ways = dp[i+1]
                if i +1 == N:
                    dp[i] = ways
                    continue
                num = int(s[i]) * 10 + int(s[i+1])
                if num <=26:
                    ways +=dp[i + 2]

                dp[i] = ways

        return dp[0]






class Solution:
    def numDecodings(self, s: str) -> int:
        """
        暴力递归版
        :param s:
        :return:

        """
        if len(s) == 0:
            return 0


        return self.process(s,0)

    def process(self,s,idx):
        """
        s[0...idx-1]已经转换玩了，不用操心了
        :param s:
        :param idx:
        :return:
        """

        if idx == len(s):
            return 1
        if s[idx] == '0':
            return 0 #不可能出现 031类似的

        # idx还有字符，且不是0
        #1）idx是0~9
        ways = self.process(s,idx+1)
        #2) idx idx+1 ->idx + 2
        if idx + 1 == len(s):
            #判断一下是不是idx+1就越界了,如果是，那2)其实就不用考虑了
            return ways
        num = int(s[idx]) * 10 + int(s[idx+1])
        # num > 26
        if num <= 26:
            ways +=self.process(s,idx + 2)

        return ways















