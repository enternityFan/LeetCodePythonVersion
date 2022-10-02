# @Time : 2022-10-02 11:27
# @Author : Phalange
# @File : 6195. 对字母串可执行的最大删除数.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D



class Solution:
    def __init__(self):
        self.ans = 0
        self.dict = {} # 记录一下，我走到这个子串，我需要的次数
    def deleteString(self, s: str) -> int:


        def process(tmp,times):
            if tmp == "":
                self.ans = max(self.ans,times)
                return times
            flag = 0
            if tmp in self.dict:
                return self.dict[tmp]

            mystr = ""
            for i in range(len(tmp)//2 + 1):
                mystr +=tmp[i]
                if tmp[i+1:] in self.dict:
                    break
                if mystr == tmp[i+1:2*i+2]:
                    flag = 1
                    self.dict[tmp[i+1:]] = process(tmp[i+1:],times+1)
                    break
            if flag == 0:
                self.dict[tmp] = times
                self.ans = max(self.ans,times + 1)
                return times
        process(s,0)
        return self.ans


print(Solution().deleteString("abcabcdabc"))