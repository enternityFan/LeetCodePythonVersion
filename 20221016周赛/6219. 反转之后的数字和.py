#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/10/16 10:35
# @Author  : HuntingGame
# @FileName: 6219. 反转之后的数字和.py
# @Software: PyCharm
# C'est la vie. Enjoy ur day ! :D


class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        if num == 0:
            return True


        for i in range(num+1):
            if i + int(str(i)[::-1]) == num:
                return True



        return False

print(Solution().sumOfNumberAndReverse(2))
print(Solution().sumOfNumberAndReverse(0))
print(Solution().sumOfNumberAndReverse(6))