#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：6222. 美丽整数的最小增量.py
@Author ：HuntingGame
@Date ：2022-10-30 10:44 
C'est la vie!!! enjoy ur day :D
'''


class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        i = 0
        if target>=108:
            return 0
        # tlist = []
        # tmptarget = target
        # while tmptarget:
        #     if tmptarget >= 9:
        #         tlist.append(9)
        #         tmptarget -=9
        #     else:
        #         tlist.append(tmptarget)
        #         tmptarget =0
        while 1:
            strtmp = [int(c) for c in str(n)]
            tmp = sum(strtmp)
            if tmp <=target:
                return i

            tmp_target = target
            curval = n
            newstrtmp = []
            #位小的不处理，位大于target的处理j
            for k in range(len(strtmp)):
                if strtmp[k] < tmp_target:# 因为产生进位，这里智能小于

                    tmp_target -=strtmp[k]
                    newstrtmp.append(strtmp[k])
                else:
                    i +=((10 ** (len(strtmp) - k)-curval) // (10 **(len(strtmp)-k-1))) * (10 ** (len(strtmp) -k -1)) #化为0
                    tmp_target -=1
                    if len(newstrtmp) == 0:
                        newstrtmp.append(1)
                    else:
                        for i in range(len(newstrtmp)-1,0,-1):

                            newstrtmp[i] +=1
                            if newstrtmp[i] >=10:
                                newstrtmp[i-1] +=1
                                newstrtmp[i] %=10
                        if newstrtmp[0] >=10:
                            newstrtmp.insert(0,1)
                        newstrtmp.append(0)

                curval -=strtmp[k] * (10 ** (len(strtmp) - k - 1))
            n = n + eval("".join([str(i) for i in newstrtmp]))
            print(n)




        return i


print(Solution().makeIntegerBeautiful(467,6))
print(Solution().makeIntegerBeautiful(74722,6))

