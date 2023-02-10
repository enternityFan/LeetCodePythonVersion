#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：395. 至少有 K 个重复字符的最长子串.py
@Author ：HuntingGame
@Date ：2023-02-10 8:19 
C'est la vie!!! enjoy ur day :D
'''
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        """
        因为只有小写字符，所以可以遍历26个字母，来看
        窗口为i中字符数，至少k个的结果，最后都求个max。




        :param s:
        :param k:
        :return:
        """
        maxval = 0
        for require in range(1,27):
            #要求窗口中必须含有require个字符，得到的答案
            cnts = [0] * 26
            collect = 0#目前窗口内出现的字符种类
            satisfy = 0#目前窗口内出现次数>=k次的字符，满足了几种
            R = -1
            for L in range(len(s)):
                if maxval > len(s) - L:
                    break
                while R + 1<len(s) and not (collect == require and cnts[ord(s[R+1]) - ord('a')]==0):
                    #如果不越界且不达标，往右阔
                    R+=1
                    if cnts[ord(s[R]) - ord('a')] == 0:
                        collect +=1 #新来了一个种类。
                    if cnts[ord(s[R]) - ord('a')] == k-1:
                        satisfy +=1
                    cnts[ord(s[R]) - ord('a')] +=1
                if satisfy == require:
                    #窗口内有satisfy种字符出现次数>=k
                    maxval = max(maxval,R-L+1)

                if cnts[ord(s[L]) - ord('a')] == 1:
                    collect -=1
                if cnts[ord(s[L]) - ord('a')] == k:
                    satisfy-=1
                cnts[ord(s[L]) - ord('a')] -=1

        return maxval


