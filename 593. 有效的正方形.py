# @Time : 2022-07-29 11:50
# @Author : Phalange
# @File : 593. 有效的正方形.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:

    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def distance(p1: List[int], p2: List[int]):
            return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5



        d1 = distance(p1,p2)
        d2 = distance(p1,p3)
        d3 = distance(p1,p4)
        d4 = distance(p2,p3)
        d5 = distance(p3,p4)
        d6 = distance(p2,p4)
        Ds =[d1,d2,d3,d4,d5,d6]

        mydict = {}
        kind = set(Ds)
        if len(kind) !=2 or 0 in Ds:
            return False
        for each in Ds:
            if each in mydict:
                mydict[each]+=1
                if mydict[each] == 4:
                    return True
            else:
                mydict[each]=1
        return False

s = Solution()
p1 = [0,0]
p2 = [1,1]
p3 = [1,0]
p4 = [0,1]
print(s.validSquare(p1,p2,p3,p4))








