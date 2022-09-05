# @Time : 2022-09-05 19:03
# @Author : Phalange
# @File : 1662. 检查两个字符串数组是否相等.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1) == "".join(word2)
