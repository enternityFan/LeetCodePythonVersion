#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/2/20 13:13
# @Author  : HuntingGame
# @FileName: 788. 旋转数字.py
# @Software: PyCharm
# C'est la vie. Enjoy ur day ! :D
class Solution:
    def rotatedDigits(self, n: int) -> int:

        ans = 0
        dp = [2,2,1,0,0,1,1,0,2,1,2]#2表示如果和1的组合的话，就是了；0表示出现就不行；1表示行的
        if n <=10:
            ans = 0
            for i in range(n+1):
                ans += 1 if dp[i] == 1 else 0
            return ans
        ans = 4
        for i in range(11,n+1):
            tmp = str(i)
            highBit = int(tmp[0])
            other = int(tmp[1:])
            if dp[highBit] == 0:
                dp.append(0)
            elif dp[highBit] == 2:
                dp.append(dp[other])
            else:
                if dp[other] == 0:
                    dp.append(0)
                else:
                    dp.append(1)
            if dp[-1] == 1:
                print(i)
                ans +=1
        return ans

print(Solution().rotatedDigits(857))



