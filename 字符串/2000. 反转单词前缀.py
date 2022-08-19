# @Time : 2022-08-19 14:28
# @Author : Phalange
# @File : 2000. 反转单词前缀.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D



class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = word.find(ch)
        if idx == -1:
            return word
        ans = list(word[:idx+1])
        ans.reverse()
        return "".join(ans)+word[idx+1:]

print(Solution().reversePrefix("hello","e"))