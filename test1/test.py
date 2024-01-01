# coding=utf-8
"""

================================================================

author: Tan Chang 
file: test.py
date:2023/12/13

================================================================

"""
import re

# text = input()

def split_by_comma(text):
    return re.split(r',(?=(?:[^"]*"[^"]*")*[^"]*$)', text)

# text = 'a,b,"c,d",e'
text = "bb=\"gvghghhg,jhjh=90,hghf=\"klkjkj\", h=9"
result = split_by_comma(text)
print(result)

# pattern = r"['\"]([^'\"]*)['\"]"
# # result = re.findall(pattern, text)
# if bool(re.match(r"(?<![a-zA-Z0-9])['\"]([^'\"]*)['\"](?![a-zA-Z0-9])", text)):
# if bool(re.match(r"^'.*'$",text)):
#
#         print(text + "为合法变量且是字符串")
# if bool(re.match(r"^(\+?-?\d+(\.\d+)?|0(\.\d+)?)$", text)):
#     # if bool(re.match(r"(['\"])(.*?)\1", text)):
#     print(text + "为合法变量且是实型")

import re

import re

# s = ["10;"]
# s_1 = s[0].pop(-1)
# print(s_1)
# # result = re.split(r';', s)
# # print(result)


