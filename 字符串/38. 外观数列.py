# @Time : 2022-07-29 7:47
# @Author : Phalange
# @File : 38. 外观数列.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D





class Solution:
    def countAndSay(self, n: int) -> str:
        arr = [0,"1"]
        for i in range(2,n+1):
            temp = ""
            prev = 0
            curr = str(arr[i-1]) # '11'
            c = 0
            for j in range(len(curr)):
                if prev == 0:
                    c +=1
                    prev = curr[j]
                elif prev == curr[j]:
                    c +=1
                else:
                    temp +=str(c)
                    temp +=str(prev)
                    c = 1
                    prev = curr[j]

            if c !=0:

                temp += str(c)
                temp += str(prev)

            arr.append(temp)

        return arr[n]



s = Solution()

print(s.countAndSay(2))
print(s.countAndSay(3))
print(s.countAndSay(4))
print(s.countAndSay(5))