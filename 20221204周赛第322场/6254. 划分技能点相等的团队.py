#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：6254. 划分技能点相等的团队.py
@Author ：HuntingGame
@Date ：2022-12-04 10:35 
C'est la vie!!! enjoy ur day :D
'''
import collections
from typing import List


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        if n == 2:
            return skill[0] * skill[1]
        if sum(skill) % (n // 2) !=0:
            return -1
        target = sum(skill) // (n // 2)
        ans = []
        skill.sort()
        mycnter = collections.Counter(skill)
        i = 0
        while(i < n//2):
            #使用二分法寻找另外一个目标
            l = n // 2
            r = n-1
            flag = 0
            while (l <=r):
                mid = l + (r - l) // 2
                print(mid,i)
                if skill[mid] == target - skill[i] :
                    if mycnter[skill[i]] == mycnter[skill[mid]]:
                        if skill[i] !=skill[mid]:
                            for _ in range(mycnter[skill[i]]):
                                ans.append([skill[i],skill[mid]])
                            i +=mycnter[skill[i]]
                        else:
                            for _ in range(mycnter[skill[i]] // 2):
                                ans.append([skill[i], skill[mid]])
                            i += mycnter[skill[i]]//2
                        flag = 1
                        break
                    else:
                        return -1
                    flag = 1
                    break
                elif skill[mid] < target - skill[i]:
                    l = mid +1
                else:
                    r = mid - 1
            if not flag:
                return -1
        res = 0
        print(ans)
        for each in ans:
            res +=each[0] * each[1]

        return res





print(Solution().dividePlayers([20,20,17,9,7,19,12,12]))