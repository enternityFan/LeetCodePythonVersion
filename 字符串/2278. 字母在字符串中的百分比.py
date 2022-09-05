# @Time : 2022-09-05 19:06
# @Author : Phalange
# @File : 2278. 字母在字符串中的百分比.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import collections


class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        mycounter = collections.Counter(s)
        return mycounter[letter]*100 // len(s)