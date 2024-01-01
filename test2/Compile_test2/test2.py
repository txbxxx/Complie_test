#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
======================================================
@Project ：Compile_test2
@File    ：test2.py
@IDE     ：PyCharm
@Author  ：tanchang
@Date    ：2023/12/27 10:49
Text     ：GoodGood学习,天天UPUP
给定LL(1)文法和分析表，输入字符串检查它是否匹配LL(1)文法($表示空串)
=======================================================
"""
from analysis_table import analysis_table
from prettytable import PrettyTable


# 分析文法中每个字符，拆分
def consist(all_end_list, end_list, no_end_list, analysis):
    # 分开左部右部、终结符、非终结符
    for line in open('LL(1)'):
        # 删除换行
        line = line.rstrip('\n')
        analysis["l"].append(line[0])  # 将左部元素全部加入左部
        if "|" in line[3:]:  # 判断右部元素是否有 "|" 有就拆分
            for char in line[3:].split("|"):
                analysis["r"].append(char)  # 遍历拆分的元素然后加入到右部元素表
        else:
            analysis["r"].append(line[3:])
        no_end_list.append(line[0])  # 非终结符列表
        line[3:].rstrip("|")
        for char in line[3:]:
            if not char.isupper():
                all_end_list.append(char)  # 所有终结符列表
                if char != '$':
                    end_list.append(char)  # 所有$的终极符列表


def analysis_function(str, GS, no_end_list, analy_list):
    i = 1
    left = str[::-1]  # 将输入的字符串反过来赋予它，便于pop删除
    stack = ['#', no_end_list[0]]  # 栈堆
    while len(left) > 0:  # 当剩余未分析的字符串长度大于0时，继续进行分析
        a = []
        a.append(i)
        # 分析栈
        init = ""  # 初始化,第一次是输出在栈里面的值，第二次是输出正序的字符串值
        for single in stack:  # 遍历分析栈中的每个元素
            init += single  # 将分析栈中的元素逐个添加到输出字符串out中
        a.append(init)  # 将入栈的加入到列表中
        # 剩余输入串
        init = ""
        init = left[::-1]
        a.append(init)  # 将字符加入到列表
        char1 = stack[len(stack) - 1]  # 获取分析栈顶部的元素
        char2 = left[len(left) - 1]  # 获取剩余未分析的字符串的最后一个字符
        if (char1 == char2) and (char1 == '#'):  # 如果分析栈顶部的元素与剩余未分析的字符串的最后一个字符相同且为'#'
            a.append("接受语法")
            analy_list.append(a)
            break
        if char1 == char2:  # 如果分析栈顶部的元素与剩余未分析的字符串的最后一个字符相同
            stack.pop()  # 弹出分析栈顶部的元素
            left = left[:-1]  # 移除剩余未分析的字符串的最后一个字符
            a.append("匹配")
        elif GS.get(char1) and GS[char1].get(char2) is not None:  # 读取分析表内的数据如果分析表不为空
            right_str = GS[char1][char2]  # 获取产生式的右侧字符串
            stack.pop()  # 弹出分析栈顶部的元素
            if right_str[3:] != "$":  # 如果产生式的右侧字符串不是'$'
                copy = right_str[3:][::-1]  # 将产生式的右侧字符串反过来赋值给copy
                for single in copy:  # 遍历copy中的每个元素
                    stack.append(single)  # 将copy中的元素逐个添加到分析栈中
            a.append(right_str)
        else:  # 如果以上条件都不满足
            a.append("出错")
            analy_list.append(a)
            break
        i += 1
        analy_list.append(a)


if __name__ == '__main__':
    GS = analysis_table()
    all_end_list = []  # 所有终结符
    end_list = []  # 出空串外所有终结符
    no_end_list = []  # 终结符集
    analysis = {"r": [], "l": []}  # r为右部，l为左部
    # str = "m+m*m#"
    str = input("请输入字符串：")
    if not str.endswith("#"):
        str = str+"#"
    analy_list = []  # 大列表，里面存储着过程表中的每一行数据
    consist(all_end_list, end_list, no_end_list, analysis)
    analysis_function(str, GS, no_end_list, analy_list)
    print("\n")
    table = PrettyTable()
    # 添加表头
    table.field_names = ["步骤  ", "   分析栈    ", "   剩余输入串     ", "   推导式    "]
    for i in analy_list:
        table.add_row(i)
    print(table)
