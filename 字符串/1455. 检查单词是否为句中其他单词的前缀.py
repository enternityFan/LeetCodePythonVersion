# @Time : 2022-08-21 21:06
# @Author : Phalange
# @File : 1455. 检查单词是否为句中其他单词的前缀.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D



class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        ls = sentence.split(" ")
        ans = -1

        for i,each in enumerate(ls):
            if len(each) >= len(searchWord) and each[:len(searchWord)] == searchWord:
                if ans == -1:
                    ans = i+1
                    break
        return ans