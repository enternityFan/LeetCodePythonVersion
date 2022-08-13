# @Time : 2022-08-13 17:27
# @Author : Phalange
# @File : 557. 反转字符串中的单词 III.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D


class Solution:
    def reverseWords(self, s: str) -> str:
        return " " .join([each[::-1] for each in s.split(" ")])