#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：8. 字符串转换整数 (atoi).py
@Author ：HuntingGame
@Date ：2023-02-01 13:38 
C'est la vie!!! enjoy ur day :D
'''
class Solution:
    def myAtoi(self, s: str) -> int:
        if s == "":
            return 0
        s = self.removeHeadZero(s.strip())
        if s == "":
            return 0
        if not self.isValid(s):
            #验证是不是有效的整数
            return 0
        # 能到这里的string，才是正常的整数的形式
        posi = False if s[0] == '-' else True
        minq = (-2 ** 31) // 10 #最小数的除数
        minr = (-2 ** 31) % 10 #最小数的余数
        res = 0
        cur = 0
        start = 0 if s[0] not in ["-","+"] else 1
        for i in range(start,len(s)):
            cur = - int(s[i])#转换为负数
            if (res < minq) or ((res == minq) and cur < minr):
                return 2**31 - 1 if posi else -2 ** 31
            res = res * 10 + cur

        if posi and res <= -2 ** 31:
            return 2 ** 31 - 1
        if not posi and res <= -2 **31:
            return -2 ** 31


        return -res if posi else res






        return s


    def removeHeadZero(self,s:str):
        r = (s.find("+")!=-1 or s.find("-")!=-1)
        start = 1 if r else 0# 判断有没有符号，来看是不是要跳过
        idx1 = 0
        for i in range(start,len(s)):
            if s[i] !='0':
                idx1 = i
                break
        e = -1
        for i in range(len(s)-1,start-1,-1):
            if s[i] <'0' or s[i] > '9':
                e = i
        if e == -1:
            return s[0] + s[idx1:] if r else s[idx1:]
        return s[0] +s[idx1:e] if r else s[idx1:e]

    def isValid(self, s):
        if s[0] !='-' and s[0] !='+' and (s[0] <'0' or s[0] > '9'):
            #第一个不是数字
            return False
        if (s[0] == '-' or s[0] == '+') and len(s) == 1:
            # 只有一个符号
            return False
        for i in range(1,len(s)):
            if (s[i] not in "0123456789"):
                return False
        return True
print(Solution().myAtoi("2147483648"))

