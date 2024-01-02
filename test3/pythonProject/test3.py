#!/usr/bin/env python
# -*- coding: UTF-8 or GBK -*-
"""
======================================================
@Project ：pythonProject 
@File    ：test3.py
@IDE     ：PyCharm 
@Author  ：tanchang
@Date    ：2023/12/28 16:39 
Text     ：GoodGood学习,天天UPUP
编译原理算法优先语法分析
=======================================================
"""

from analysis_table import analysis_table
from prettytable import PrettyTable
import string


def analysis(str, table, right_list, aList):
    stack = ['#']  # 分析栈，栈顶为#
    strT = str[::-1]  # 倒序，方便删除
    i = 1  # 步骤
    while len(strT) > 0:
        bList = [i]
        up = len(stack) - 1  # 指向栈顶的指针
        if stack[up].isupper():  # 如果栈顶为大小字母就找它的下一个看看是不是终结符
            for k in reversed(range(len(stack) - 1)):
                if not stack[k].isupper():
                    # print(stack[k])
                    up = k
                    break
        init = ""
        for single in stack:  # 栈顶加入总表
            init += single
        bList.append(init)
        init = ""
        init = strT[::-1]  # 当前输入
        bList.append(init)
        char1 = stack[up]  # 当前栈顶字符
        char2 = strT[len(strT) - 1]  # 当前输入字符
        if table.get(char1) and table.get(char1).get(char2) is not None:
            if table.get(char1).get(char2) == '<':  # 如果读取为<则是移进
                bList.append('<')
                stack.append(char2)  # 当前输入字符入栈
                strT = strT[:-1]  # 删除当前入栈字符
                bList.append("移进")
            elif table.get(char1).get(char2) == '>':
                bList.append('>')
                # stack[up] = 'N'
                bList.append("归约")

                # 判断栈顶的终结符和它后面那个终结符的大小关系，规约就将第二个字符后的都归约为N
                c = -1
                first = 0
                end = 0
                while -len(stack) <= i:
                    if not stack[c].isupper():
                        if first == 0:
                            first = c
                        else:
                            end = c
                        if first != 0 and end != 0:
                            if table.get(stack[end]).get(stack[first]) == '<':
                                stack[c + 1:] = 'N'
                                break
                            else:
                                first = end
                                end = 0
                    c -= 1
            # 移进
            elif table.get(char1).get(char2) == '=':
                bList.append('=')
                stack.append(char2)
                strT = strT[:-1]
                bList.append("移进")
            else:
                bList.append("报错")
                bList.append(" ")
                aList.append(bList)
                break
        elif char1 == char2 and char1 == "#":
            bList.append("接受")
        else:
            bList.append("报错")
            bList.append(" ")
            aList.append(bList)
            break
        i += 1
        aList.append(bList)


def list_arrg(right_list):
    for line in open("文法"):
        line = line.rstrip('\n')
        # print(line)
        if "'" not in line[:2]:  ##如果存在 ' 号的
            if "|" in line[3:]:  # 判断右部元素是否有 "|" 有就拆分
                for char in line[3:].split("|"):
                    upper = string.ascii_uppercase  # 获取当前右部包含所有的大写字母的数
                    tranS = str.maketrans(upper, 'N' * len(upper))  # 将他们都切换为N 我这里多此一举了，写到一半就发现了更好的办法1
                    a = char.translate(tranS)
                    right_list.append(a)
            else:  # 没有就直接添加
                upper = string.ascii_uppercase
                tranS = str.maketrans(upper, 'N' * len(upper))
                a = line[3:].translate(tranS)
                right_list.append(a)
        else:  # 不存在 ‘ 号的
            if "|" in line[4:]:  # 判断右部元素是否有 "|" 有就拆分
                for char in line[4:].split("|"):
                    upper = string.ascii_uppercase
                    tranS = str.maketrans(upper, 'N' * len(upper))
                    a = char.translate(tranS)
                    right_list.append(a)
            else:
                upper = string.ascii_uppercase
                tranS = str.maketrans(upper, 'N' * len(upper))
                a = line[4:].translate(tranS)
                right_list.append(a)
    print(right_list)


if __name__ == '__main__':
    right_list = []
    aList = []
    # str = "i+(i+i)"
    str = input("请输入字符串:")
    if not str.endswith("#"):
        str += '#'
    table = analysis_table()
    list_arrg(right_list)  # 计算右部列表
    analysis(str, table, right_list, aList)  # 计算分析表
    tableSF = PrettyTable()
    tableSF.field_names = ["步骤", "  分析栈  ", "  当前输入  ", "  优先关系  ", "  操作  "]
    for i in aList:
        # print(i)
        tableSF.add_row(i)
    print(tableSF)
