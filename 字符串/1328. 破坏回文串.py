#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：1328. 破坏回文串.py
@Author ：HuntingGame
@Date ：2022-11-08 8:12 
C'est la vie!!! enjoy ur day :D
'''

class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1:
            return ""
        idx = -1
        flag = 0

        for i in range(n):
            if palindrome[i] !='a':
                if n % 2 == 0 or (n % 2 != 0 and i != n // 2):
                    idx = i
                    flag = 1
                    break
        if flag == 0:
            return palindrome[:-1] + chr(ord(palindrome[-1]) + 1)
        return palindrome[:idx] + 'a' + palindrome[idx+1:]


print(Solution().breakPalindrome("bbb"))
