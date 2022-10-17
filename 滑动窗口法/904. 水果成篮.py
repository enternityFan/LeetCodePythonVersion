# @Time : 2022-10-17 11:50
# @Author : Phalange
# @File : 904. 水果成篮.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ans = 0
        s = 0
        e = 1
        n = len(fruits)
        if n ==1:
            return 1
        #set_windows = set(fruits[e],fruits[s])
        set_windows = {}
        for i in range(2):
            if fruits[i] not in set_windows:
                set_windows[fruits[i]] = 0
            set_windows[fruits[i]] +=1


        for i in range(2,n):
            if fruits[i] in set_windows:
                set_windows[fruits[i]] +=1
                e +=1
            elif len(set_windows) == 1:
                set_windows[fruits[i]] = 1
                e +=1
            else:
                ans = max(ans,e-s+1)
                for j in range(s,e+1):
                    set_windows[fruits[j]]-=1
                    if set_windows[fruits[j]] == 0:
                        set_windows.pop(fruits[j])
                        s = j+1
                        break
                set_windows[fruits[i]] = 1
                e+=1
        ans = max(ans,e-s+1)
        return ans


fruits = [3,3,3,1,2,1,1,2,3,3,4]

#fruits = [1,2,1]
print(Solution().totalFruit(fruits))



