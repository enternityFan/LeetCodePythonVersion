# @Time : 2022-08-01 20:22
# @Author : Phalange
# @File : 1486. 数组异或操作.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = 0
        for i in range(n):
            nums ^= (start + 2 * i)


        return nums