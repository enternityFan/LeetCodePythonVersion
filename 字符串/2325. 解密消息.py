# @Time : 2022-08-19 10:40
# @Author : Phalange
# @File : 2325. 解密消息.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D



class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mymap = {" ":" "}
        code = ord("a")
        for c in key:
            if c not in mymap:
                mymap[c] = chr(code)
                code +=1
        ans = ""
        for c in message:

            ans +=mymap[c]
        return ans