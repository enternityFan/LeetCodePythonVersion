# @Time : 2022-09-07 11:33
# @Author : Phalange
# @File : 1592. 重新排列单词间的空格.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D

class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = []
        word = ""
        space = 0
        for c in text:
            if c == " ":
                space +=1
                if word !="":
                    words.append(word)
                    word = ""
            else:
                word +=c
        if word !="":
            words.append(word)
        if len(words)==1:
            return words[0] + " "*space
        print(words)
        print(space)
        yushu = space % (len(words)-1)
        ans = ""
        for i in range(len(words)-1):
            ans +=words[i]
            ans +=" " * (space // (len(words)-1))

        ans +=words[-1]
        ans += " " * yushu
        return ans
print(Solution().reorderSpaces("  jhbqunnzo "))


