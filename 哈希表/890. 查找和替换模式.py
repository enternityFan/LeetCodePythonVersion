# @Time : 2022-07-30 17:32
# @Author : Phalange
# @File : 890. 查找和替换模式.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = []
        for i in range(len(words)):
            if len(pattern) == len(words[i]) and len(set(words[i])) == len(set(pattern)) == len(set(zip(words[i],pattern))):
                res.append(words[i])

        return res
