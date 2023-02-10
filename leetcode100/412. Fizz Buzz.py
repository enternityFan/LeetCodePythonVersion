#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：412. Fizz Buzz.py
@Author ：HuntingGame
@Date ：2023-02-10 8:57 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1,n+1):
            if i % 15 == 0:
                ans.append("FizzBuzz")
            elif i % 5 == 0:
                ans.append("Buzz")
            elif i % 3 == 0:
                ans.append("Fizz")
            else:
                ans.append(str(i))
        return ans