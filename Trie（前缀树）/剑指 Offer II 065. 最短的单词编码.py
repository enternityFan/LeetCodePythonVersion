# @Time : 2022-08-04 10:28
# @Author : Phalange
# @File : 剑指 Offer II 065. 最短的单词编码.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import collections
from typing import List


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        """
        存储后缀就行了
        :param words:
        :return:
        """
        words = sorted(words,key=lambda x:len(x),reverse=True)
        trie = {}
        result = 0
        for word in words:
            cur = trie
            word = word[::-1]
            cnt = 0
            flag = 0 # 判断这个单词是否是别人的后缀,默认是
            for c in word:
                if c not in cur:
                    cur[c] = {}
                    flag = 1 #此时不是别人的子串
                cur = cur[c]
                cnt +=1
            cur['#'] = {cnt+1}
            if flag == 1:
                result =result + cnt + 1

        # for key,value in trie.items():
        #     k = key
        #     v = value
        #     tmp = 0 # 记录对于这个开始的最长的路径
        #     while k !='#':

        return result


print(Solution().minimumLengthEncoding(["time","me","bell"]))
print(Solution().minimumLengthEncoding(["me","time","bell"]))