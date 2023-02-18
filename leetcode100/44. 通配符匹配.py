#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：44. 通配符匹配.py
@Author ：HuntingGame
@Date ：2023-02-02 14:11 
C'est la vie!!! enjoy ur day :D
'''

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        这个是dp的方法,不过优化了斜率，这个的效果最好的。
        :param s:
        :param p:
        :return:
        """
        if s == "" and p == "":
            return True
        dp = [[False for _ in range(len(p)+1)] for i in range(len(s)+1)]
        N = len(s)
        M = len(p)
        #basecase
        dp[N][M] = True
        for pi in range(M-1,-1,-1):
            dp[N][pi] = (p[pi] == '*' and dp[N][pi+1])

        #下面要具体的改si pi了。
        for si in range(N-1,-1,-1):

            for pi in range(M-1,-1,-1):
                # si,pi
                if p[pi] != '?' and p[pi] != '*':
                    dp[si][pi] =  (s[si] == p[pi]) and dp[si+1][pi+1]
                    continue
                if p[pi] == '?':
                    dp[si][pi] = dp[si+1][pi+1]
                    continue

                # [pi] == '*'
                dp[si][pi] = dp[si][pi + 1] or dp[si + 1][pi]  # 此时他只依赖于这两个位置


        return dp[0][0]


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        这个是dp的方法
        :param s:
        :param p:
        :return:
        """
        if s == "" and p == "":
            return True
        dp = [[False for _ in range(len(p)+1)] for i in range(len(s)+1)]
        N = len(s)
        M = len(p)
        #basecase
        dp[N][M] = True
        for pi in range(M-1,-1,-1):
            dp[N][pi] = (p[pi] == '*' and dp[N][pi+1])

        #下面要具体的改si pi了。
        for si in range(N-1,-1,-1):

            for pi in range(M-1,-1,-1):
                # si,pi
                if p[pi] != '?' and p[pi] != '*':
                    dp[si][pi] =  (s[si] == p[pi]) and dp[si+1][pi+1]
                    continue
                if p[pi] == '?':
                    dp[si][pi] = dp[si+1][pi+1]
                    continue

                # 如果是*的话，就要多考虑考虑
                for length in range(len(s) - si + 1):
                    if dp[si + length][pi + 1]:
                        dp[si][pi] = True
                        break


        return dp[0][0]

    def process(self,s,p,si,pi):
        """
        s[si....]能否被p[pi...]凑出来
        :param s:
        :param p:
        :param si:
        :param pi:
        :return:
        """
        if si == len(s):
            if pi == len(p):
                return True
            else:
                return p[pi] == '*' and self.process(s,p,si,pi+1)

        if pi == len(p):
            return si == len(s)

        #s从si触发，p从pi出发
        #s[si]只可能是小写字幕，p[pi]可能是小写字幕，？，*
        if p[pi] !='?' and p[pi] !='*':
            return (s[si] == p[pi]) and self.process(s,p,si+1,pi+1)
        if p[pi] == '?':
            return self.process(s,p,si+1,pi+1)
        #如果是*的话，就要多考虑考虑
        for length in range(len(s) - si+1):
            if self.process(s,p,si+length,pi+1):
                return True

        return False









class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        这个是最原始的暴力递归，只会超时一些
        :param s:
        :param p:
        :return:
        """
        if s == "" and p == "":
            return True

        return self.process(s,p,0,0)




    def process(self,s,p,si,pi):
        """
        s[si....]能否被p[pi...]凑出来
        :param s:
        :param p:
        :param si:
        :param pi:
        :return:
        """
        if si == len(s):
            if pi == len(p):
                return True
            else:
                return p[pi] == '*' and self.process(s,p,si,pi+1)

        if pi == len(p):
            return si == len(s)

        #s从si触发，p从pi出发
        #s[si]只可能是小写字幕，p[pi]可能是小写字幕，？，*
        if p[pi] !='?' and p[pi] !='*':
            return (s[si] == p[pi]) and self.process(s,p,si+1,pi+1)
        if p[pi] == '?':
            return self.process(s,p,si+1,pi+1)
        #如果是*的话，就要多考虑考虑
        for length in range(len(s) - si+1):
            if self.process(s,p,si+length,pi+1):
                return True

        return False

















