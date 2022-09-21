#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePythonVersion 
@File ：316. 去除重复字母.py
@Author ：HuntingGame
@Date ：2022/9/21 12:35 
C'est la vie!!! :)
'''
import collections


"""
[1,2,4,3,5]


1

"""
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        remain_counter = collections.Counter(s)
        for c in s:
            if c not in stack:
                while stack and c < stack[-1] and remain_counter[stack[-1]] > 0:
                    stack.pop()
                stack.append(c)
            remain_counter[c] -=1

        return "".join(stack)

print(Solution().removeDuplicateLetters("cbacdcbc"))