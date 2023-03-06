#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：剑指 Offer 48. 最长不含重复字符的子字符串.py
@Author ：HuntingGame
@Date ：2023-03-06 19:08 
C'est la vie!!! enjoy ur day :D
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        record = [0] * 256 #存放ascii码上一次出现的位置。
        ans = 0
        cur = 0#当前长度
        pre = -1
        for i in range(len(s)):
            pre = max(pre,record[ord(s[i])])
            cur = i - pre
            ans = max(ans,cur)
            record[ord(s[i])] = i

        return ans

