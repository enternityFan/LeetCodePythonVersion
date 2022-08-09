# @Time : 2022-08-09 18:13
# @Author : Phalange
# @File : 1974. 使用特殊打字机键入单词的最少时间.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D


class Solution:
    def minTimeToType(self, word: str) -> int:
        ans = 0
        n = len(word)
        # if n == 1:
        #     return 1 + min(ord(word[0]) - ord('a'),ord('a')+26-ord(word[0]))
        if word[0] > 'a':
            ans += 1 + min(ord(word[0]) - ord('a'), ord('a') + 26 - ord(word[0]))
        else:
            ans += 1 + min(ord('a') - ord(word[0]), ord(word[0]) + 26 - ord('a'))
        prev = word[0]

        for i in range(1,n):
            if word[i] > prev:
                ans += 1 + min(ord(word[i]) - ord(prev), ord(prev) + 26 - ord(word[i]))
            else:
                ans += 1 + min(ord(prev) - ord(word[i]), ord(word[i]) + 26 - ord(prev))
            prev = word[i]
        return ans

print(Solution().minTimeToType("bza"))