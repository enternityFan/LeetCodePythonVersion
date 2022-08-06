# @Time : 2022-08-06 7:52
# @Author : Phalange
# @File : 1408. 数组中的字符串匹配.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and words[j].find(words[i]) !=-1:
                    ans.append(words[i])
                    break
        return ans

print(Solution().stringMatching(["mass","as","hero","superhero"]))