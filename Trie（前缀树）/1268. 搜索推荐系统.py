# @Time : 2022-08-04 11:17
# @Author : Phalange
# @File : 1268. 搜索推荐系统.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List

class Trie:
    def __init__(self):
        self.child = dict()
        self.words = list()



class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for word in products:
            cur = trie
            for c in word:
                if c not in cur.child:
                    cur.child[c] = Trie()
                cur = cur.child[c]
                cur.words.append(word)
                cur.words.sort()
                if len(cur.words) >3:
                    cur.words.pop()

        result =[]
        flag = False
        cur = trie
        for i in range(len(searchWord)):
            if flag or searchWord[i] not in cur.child:
                result.append(list())
                flag = True
            else:
                cur = cur.child[searchWord[i]]
                result.append(cur.words)

        return result

products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"
products = ["baggage","banner","box","cloths"]
searchWord = "bags"

print(Solution().suggestedProducts(products,searchWord))