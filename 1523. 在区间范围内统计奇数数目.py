# @Time : 2022-07-29 11:08
# @Author : Phalange
# @File : 1523. 在区间范围内统计奇数数目.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D


class Solution:
    def countOdds(self, low: int, high: int) -> int:
       return (high - low + 1)//2 if (high-low+1) % 2 == 0 else (high - low + 1) //2 + 1 if low % 2 != 0 else (high - low + 1 ) //2