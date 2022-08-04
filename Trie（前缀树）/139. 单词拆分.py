# @Time : 2022-08-04 14:07
# @Author : Phalange
# @File : 139. 单词拆分.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        trie = {}
        for word in wordDict:
            cur = trie
            for c in word:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            cur['#'] = {}
        cur = trie
        for c in s:
            if c not in cur:
                return False
            cur = cur[c]
            if '#' in cur and cur['#'] == {}:

                cur = trie
        if '#' not in cur:
            return False

        return True

print(Solution().wordBreak("aaaaaaa","aa"))
print(Solution().wordBreak("leetcode",["leet","code"]))

