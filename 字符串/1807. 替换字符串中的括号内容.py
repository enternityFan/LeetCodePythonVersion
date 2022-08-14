# @Time : 2022-08-14 14:34
# @Author : Phalange
# @File : 1807. 替换字符串中的括号内容.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import collections
from typing import List


class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        mydict = collections.defaultdict(str)

        for each in knowledge:
            mydict[each[0]] = each[1]

        #s = s.replace("({:})".format(each[0]),each[1])
        lidx = s.find("(")
        if lidx == -1:
            #证明没有?的情况
            return s
        ridx = s.find(")")
        while lidx !=-1 and ridx !=-1:
            if s[lidx+1:ridx] in mydict:
                s = s.replace(s[lidx:ridx+1],mydict[s[lidx+1:ridx]])
            else:
                s = s.replace(s[lidx:ridx+1],"?")
            lidx = s.find("(")
            ridx = s.find(")")

        return s

s = "(name)is(age)yearsold"
knowledge = [["name","bob"],["age","two"]]
print(Solution().evaluate("c",[]))
print(Solution().evaluate(s,knowledge))