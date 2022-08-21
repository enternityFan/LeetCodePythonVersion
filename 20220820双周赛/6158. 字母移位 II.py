# @Time : 2022-08-20 23:12
# @Author : Phalange
# @File : 6158. 字母移位 II.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import collections
from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        ls = [c for c in s]
        n = len(shifts)
        shifts.sort(key=lambda x:x[0])
        #mysite = collections.defaultdict(int)
        for i in range(n):
            for j in range(shifts[i][0],shifts[i][1]+1):

                if shifts[i][2] == 1:
                    #mysite[j]+=1
                    ls[j] = chr((ord(ls[j]) - ord('a') + 1 + 26) % 26 + ord('a'))
                else:
                    #mysite[j] -= 1
                    ls[j] = chr((ord(ls[j]) - ord('a') - 1 + 26) % 26 + ord('a'))

        #for key,val in mysite.items():

            #ls[key] =chr((ord(ls[key])-ord('a')+val+26)%26 + ord('a'))

        return "".join(ls)
strs = "kzggmixsmujrprkenrivuwoytlykxtxbdexsjvczwuijfrbfdehmcgqfozlrisrute"
shifts = [[36,63,1],[23,59,0],[39,51,1],[28,54,1],[19,55,0],[36,56,1],[29,39,0],[60,60,1],[5,17,1],[38,56,1],[56,56,1],[46,62,1],[59,61,0],[2,51,0],[8,43,0],[7,50,1],[34,56,0],[65,65,0],[27,54,0],[42,49,0],[53,63,0],[6,15,0],[42,63,1],[6,25,1],[20,62,1],[1,25,1],[11,34,1],[42,48,1],[19,47,1],[52,54,0],[23,35,1],[10,47,1],[59,61,0],[59,65,0],[2,31,0],[12,57,1],[56,64,1],[13,59,0],[47,54,1],[12,56,1],[22,54,1],[21,62,1],[6,24,1],[65,65,1]]
print(Solution().shiftingLetters(strs,shifts))