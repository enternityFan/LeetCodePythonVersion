# @Time : 2022-08-19 11:14
# @Author : Phalange
# @File : 925. 长按键入.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import collections


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        cn = 0
        if set(name) !=set(typed):
            return False
        for i in range(len(typed)):
            if cn < len(name) and typed[i] != name[cn] and ((i!=0 and typed[i] !=typed[i-1]) or i==0):
                return False
            elif cn >=len(name) and typed[i] !=typed[i-1]:
                return False
            elif cn < len(name) and typed[i] == name[cn]:
                cn +=1



        return True if cn==len(name) else False
name = "rick"
typed = "kric"
print(Solution().isLongPressedName(name,typed))