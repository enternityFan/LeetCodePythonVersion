# @Time : 2022-08-13 18:00
# @Author : Phalange
# @File : 1078. Bigram 分词.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        ltext = text.split(" ")
        n = len(ltext)
        if n <3:
            return [""]
        idx = 2
        ans = []
        while idx < n:
            if ltext[idx-2] == first and ltext[idx-1] == second:
                ans.append(ltext[idx])

            idx +=1
        return ans

print(Solution().findOcurrences("we will we will rock you","we","will"))

