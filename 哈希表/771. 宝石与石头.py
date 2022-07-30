# @Time : 2022-07-29 11:24
# @Author : Phalange
# @File : 771. 宝石与石头.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum([1 if each in jewels else 0 for each in stones])