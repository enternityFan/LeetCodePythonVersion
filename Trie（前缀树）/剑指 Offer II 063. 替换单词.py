# @Time : 2022-08-04 10:22
# @Author : Phalange
# @File : 剑指 Offer II 063. 替换单词.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = {}
        for word in dictionary:
            cur = trie
            for c in word:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            cur['#'] = {}

        words = sentence.split(" ")
        for i,word in enumerate(words):
            cur = trie
            for j,c in enumerate(word):
                if '#' in cur:
                    words[i] = word[:j]
                    break
                if c not in cur:
                    break
                cur = cur[c]
        return " ".join(words)
print(Solution().replaceWords(["cat","bat","rat"],"the cattle was rattled by the battery"))