#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：20. 有效的括号.py
@Author ：HuntingGame
@Date ：2023-02-02 8:52 
C'est la vie!!! enjoy ur day :D
'''
class Solution:
    def isValid(self, s: str) -> bool:
        if s == "":
            return True
        mystack = []
        for i in range(len(s)):
            if s[i] in "([{":
                mystack.append(s[i])
            else:
                if mystack== []:
                    return False
                last = mystack.pop()
                if not ((s[i] == ')' and last =='(') or (s[i] == ']' and last =='[') or (s[i] == '}' and last =='{')):
                    return False

        return mystack ==[]

print(Solution().isValid("()[]{}"))