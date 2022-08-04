# @Time : 2022-08-04 11:40
# @Author : Phalange
# @File : 451. 根据字符出现频率排序.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import collections


class Solution1:
    def frequencySort(self, s: str) -> str:
        """
        通过哈希表实现
        :param s:
        :return:
        """
        mydict = collections.Counter(s)
        mydict = sorted(mydict.items(),key=lambda x:x[1],reverse=True)
        result = ""
        for each in mydict:
            result +=each[0] * each[1]
        return result




print(Solution1().frequencySort("Aabb"))