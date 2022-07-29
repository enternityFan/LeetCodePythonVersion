# @Time : 2022-07-29 16:35
# @Author : Phalange
# @File : 290. 单词规律.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        return len(pattern) == len(s) and (len(set(pattern)) == len(set(s)) == len(set(zip(pattern,s))))




s = Solution()
print(s.wordPattern("aba", "cat cat cat dog"))