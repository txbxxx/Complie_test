#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
======================================================
@Project ：Compile_test2
@File    ：web.py
@IDE     ：PyCharm
@Author  ：tanchang
@Date    ：2023/12/27 19:20
Text     ：GoodGood学习,天天UPUP
=======================================================
"""
import matrix
from prettytable import PrettyTable

table=PrettyTable()
table.add_column("")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = [item for row in matrix for item in row]
print(result)