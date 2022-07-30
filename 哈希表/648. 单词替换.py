# @Time : 2022-07-29 21:16
# @Author : Phalange
# @File : 648. 单词替换.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        lists = sentence.split(" ")
        # 对dictionary做一个规范化
        dictionary = sorted(dictionary,key=lambda x:len(x))#按照长度对字典进行排序



        for i in range(len(lists)):
            for j in range(len(dictionary)):
                #if lists[i].find(dictionary[j]) == 0:
                # 上面的语句速度太慢了，可以用下面的代码进行优化,速度从1700ms提升到了356ms
                if lists[i][:len(dictionary[j])] == dictionary[j]:
                    lists[i] = dictionary[j]
                    break

        return " ".join(lists)

