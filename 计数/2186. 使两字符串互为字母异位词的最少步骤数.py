# @Time : 2022-10-17 13:23
# @Author : Phalange
# @File : 2186. 使两字符串互为字母异位词的最少步骤数.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import collections


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        scnt = [0]*26
        tcnt = [0]*26
        for i in range(len(s)):
            scnt[ord(s[i]) - ord('a')] +=1
        tcnt = scnt.copy()
        for i in range(len(t)):
            if tcnt[ord(t[i]) - ord('a')] !=0:
                tcnt[ord(t[i])-ord('a')] -=1

            else:
                tcnt[ord(t[i]) - ord('a')] +=1



        return sum(tcnt)

print(Solution().minSteps("leetcode","coats"))