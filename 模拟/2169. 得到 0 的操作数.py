# @Time : 2022-08-10 21:33
# @Author : Phalange
# @File : 2169. 得到 0 的操作数.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D


class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        ops = 0
        while num1 != 0 and num2 != 0:
            if num1 >= num2:
                num1 -=num2
            else:
                num2 -=num1
            ops +=1

        return ops