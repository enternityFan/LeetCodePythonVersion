#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：1604. 警告一小时内使用相同员工卡大于等于三次的人.py
@Author ：HuntingGame
@Date ：2023-02-07 22:07 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:

        ans = []
        mydict = {}
        for i in range(len(keyName)):
            if keyName[i] not in mydict:
                mydict[keyName[i]] = []
            h = int(keyTime[i][:2])
            m = int(keyTime[i][3:])
            mydict[keyName[i]].append(h * 60 + m)

        for key,val in mydict.items():
            if len(val) < 3:
                continue
            val.sort()
            cnt = 1

            for i in range(1,len(val)):
                if val[i] - val[i-cnt] <=60:
                    cnt +=1
            if cnt >=3:
                ans.append(key)

        ans.sort()
        return ans


a = ["a","a","a","a","b","b","b","b","b","b","c","c","c","c"]
b = ["01:35","08:43","20:49","00:01","17:44","02:50","18:48","22:27","14:12","18:00","12:38","20:40","03:59","22:24"]
print(Solution().alertNames(a,b))
