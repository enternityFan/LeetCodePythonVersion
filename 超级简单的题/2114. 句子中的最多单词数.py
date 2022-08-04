# @Time : 2022-08-04 18:56
# @Author : Phalange
# @File : 2114. 句子中的最多单词数.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans = 0
        for s in sentences:
            ans = max(ans,len(s.split(" ")))
        return ans
