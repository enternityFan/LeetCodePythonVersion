# @Time : 2022-09-06 19:31
# @Author : Phalange
# @File : 2255. 统计是给定字符串前缀的字符串数目.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        ans = 0
        for each in words:
            if each == s[:len(each)]:
                ans +=1
        return ans