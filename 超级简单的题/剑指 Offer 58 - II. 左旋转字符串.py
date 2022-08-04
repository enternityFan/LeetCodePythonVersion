# @Time : 2022-08-04 18:55
# @Author : Phalange
# @File : 剑指 Offer 58 - II. 左旋转字符串.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D


class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[:n]