#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/10/19 20:23
# @Author  : HuntingGame
# @FileName: 1447. 最简分数.py
# @Software: PyCharm
# C'est la vie. Enjoy ur day ! :D
from typing import List





class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        ans =[]

        for i in range(2,n+1):
            for j in range(1,i):
                if self.findMaxCom(i,j)==1:
                    ans.append("{:}/{:}".format(j,i))

        return ans

    def findMaxCom(self,i, j):
        ans = 0
        if j > i:
            i,j = j,i

        for k in range(1,j+1):
            if i % k == 0 and j % k == 0 :
                ans = k
                if k !=1:
                    break

        return ans

print(Solution().simplifiedFractions(2))