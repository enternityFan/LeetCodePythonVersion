#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：1419. 数青蛙.py
@Author ：HuntingGame
@Date ：2022-10-18 12:52 
C'est la vie!!! enjoy ur day :D
'''


class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        ans = []
        mydict = {'r':'c','o':'r','a':'o','k':'a'}
        cnt = 0
        idx = []
        for i in range(len(croakOfFrogs)):
            c = croakOfFrogs[i]
            if c == 'c':
                flag2 = 0
                if idx !=[]:
                    ans[idx[-1]] = "c"
                    flag2 = 1
                    idx.pop()
                if flag2 == 0:
                    ans.append("c")

            else:
                flag = 0
                for i in range(len(ans)):
                    if ans[i][-1] == mydict[c]:
                        ans[i] = ans[i] + c
                        flag = 1
                        if c == 'k':
                            idx.append(i)
                        break
                if flag == 0:
                    return -1
        for i in range(len(ans)):
            if ans[i] != "croak":
                return -1
        return len(ans) - cnt

print(Solution().minNumberOfFrogs("ccrrooaakk"))