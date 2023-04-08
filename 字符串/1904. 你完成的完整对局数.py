#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：1904. 你完成的完整对局数.py
@Author ：HuntingGame
@Date ：2023-04-08 21:44 
C'est la vie!!! enjoy ur day :D
'''
class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        #把时间给转换到距离0点的绝对时间
        h1,m1 = int(loginTime.split(":")[0]),int(loginTime.split(":")[1])

        h2,m2 = int(logoutTime.split(":")[0]),int(logoutTime.split(":")[1])
        time1 = h1 * 60 + m1
        time2 = h2 * 60 + m2
        ans = 0
        flag = 0
        if time2 < time1 :
            flag = 1
            # if abs(time1 - time2) <= 12 * 60:
            #     time1, time2 = time2, time1
            #     ans +=96
            #     flag = 0

        tmp = time1 if time1 % 15 == 0 else (time1 // 15 + 1)*15
        if tmp >= 24 * 60 and flag == 1:
            flag = 0
            tmp = tmp % 24 * 60
        print(time1, time2,flag)
        while (flag == 0 and tmp <= time2) or (flag == 1 and tmp > time2):
            #print(tmp)
            ans+=1
            tmp =tmp + 15

            if tmp >= 24 * 60 and flag == 1:
                flag = 0
                tmp = tmp % 24 * 60



        return ans-1 if ans !=0 else 0
#print(Solution().numberOfRounds("09:31","10:14"))
print(Solution().numberOfRounds("23:48","23:16"))

