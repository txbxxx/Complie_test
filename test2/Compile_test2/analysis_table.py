#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
======================================================
@Project ：Compile_test2 
@File    ：analysis_table.py
@IDE     ：PyCharm 
@Author  ：tanchang
@Date    ：2023/12/27 20:15 
Text     ：GoodGood学习,天天UPUP
topic: 分析表
=======================================================
"""


def analysis_table():
    # analysis_tablen = {
    #     'S': {'m': 'AT', '+': None, '*': None, '(': 'AT', ')': None, '#': None},
    #     'A': {'m': 'BU', '+': None, '*': None, '(': 'BU', ')': None, '#': None},
    #     'T': {'m': None, '+': "+AT", '*': None, '(': None, ')': '$', '#': '$'},
    #     'U': {'m': None, '+': '$', '*': '*BU', '(': None, ')': '$', '#': '$'},
    #     'B': {'m': 'm', '+': None, '*': None, '(': '(S)', ')': None, '#': None}
    # }
    analysis_tablen = {
        'S': {'m': 'S->AT', '+': None, '*': None, '(': 'A->AT', ')': None, '#': None},
        'A': {'m': 'A->BU', '+': None, '*': None, '(': 'A->BU', ')': None, '#': None},
        'T': {'m': None, '+': "T->+AT", '*': None, '(': None, ')': 'T->$', '#': 'T->$'},
        'U': {'m': None, '+': 'U->$', '*': 'U->*BU', '(': None, ')': 'U->$', '#': 'U->$'},
        'B': {'m': 'B->m', '+': None, '*': None, '(': 'B->(S)', ')': None, '#': None}
    }
    return analysis_tablen

