# @Time : 2022-07-29 20:41
# @Author : Phalange
# @File : 面试题 16.02. 单词频率.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D


from typing import List
import collections

class WordsFrequency:

    def __init__(self, book: List[str]):
        self.book = book
        self.mydict = collections.defaultdict(int)

        for each in book:
            self.mydict[each] +=1


    def get(self, word: str) -> int:
        return self.mydict[word]


# Your WordsFrequency object will be instantiated and called as such:
# obj = WordsFrequency(book)
# param_1 = obj.get(word)
book = [["i","have","an","apple","he","have","a","pen"]]
s = WordsFrequency(book)
print(s.get('have'))