# @Time : 2022-09-20 21:32
# @Author : Phalange
# @File : 299. 猜数字游戏.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D

# class Solution:
#     def getHint(self, secret: str, guess: str) -> str:
#         """
#         ans 6
#         A:8 2 2 2
#         B:7 9 1 9
#         "8226526357"
#         "7965193296"
#         :param secret:
#         :param guess:
#         :return:
#         """
#         n = len(secret)
#         secret_dict = {}
#         guess_dict = {}
#         x,y=0,0
#         for i in range(n):
#             if guess[i] == secret[i]:
#                 x +=1
#             else:
#                 print("=================================")
#                 print(secret_dict)
#                 print(guess_dict)
#                 if guess[i] not in secret_dict :
#                     if guess[i] not in guess_dict or guess_dict[guess[i]] == 0:
#                         guess_dict[guess[i]] = 1
#                     else:
#                         guess_dict[guess[i]] +=1
#                 else:
#
#                     if secret_dict[guess[i]] != 0:
#                         y += 1
#                         secret_dict[guess[i]] -= 1
#                 if secret[i] not in guess_dict :
#                     if secret[i] not in secret_dict or secret_dict[secret[i]] == 0:
#                         secret_dict[secret[i]] = 1
#                     else:
#                         secret_dict[secret[i]] +=1
#                 else:
#
#                     if guess_dict[secret[i]] != 0:
#                         y += 1
#                         guess_dict[secret[i]] -= 1
#
#
#         return str(x) +"A" + str(y) + "B"
#
# print(Solution().getHint("8226526357","7965193296"))

# class Solution:
#     def getHint(self, secret: str, guess: str) -> str:
#
#         n = len(secret)
#         secret_dict = {}
#         guess_dict = {}
#         for i in range(n-1,-1,-1):
#             if secret[i] not in secret_dict:
#                 secret_dict[secret[i]] =[]
#             secret_dict[secret[i]].append(i)
#         x,y=0,0
#         for i in range(n):
#             if guess[i] == secret[i]:
#                 x +=1
#                 secret_dict[secret[i]].pop()
#             else:
#                 if guess[i] not in guess_dict:
#                     guess_dict[guess[i]] = []
#                 guess_dict[guess[i]].append(i)
#
#         for key,val in guess_dict.items():
#             tmp = len(val)
#             while key in secret_dict and secret_dict[key] != [] and tmp !=0:
#                 secret_dict[key].pop()
#                 tmp -=1
#                 y +=1
#
#         return str(x) +"A" + str(y) + "B"
