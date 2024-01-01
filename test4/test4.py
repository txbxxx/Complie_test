#!/usr/bin/env python
# -*- coding: UTF-8 or GBK -*-
"""
======================================================
@Project ：test4 
@File    ：test4.py
@IDE     ：PyCharm 
@Author  ：tanchang
@Date    ：2024/1/1 14:43 
Text     ：GoodGood学习,天天UPUP
LR0文法
=======================================================
"""

from table import table
from prettytable import PrettyTable


def consist(table, LR0, right_size, right):
    for line in open('LR0'): # 读取文法
        line = line.rstrip('\n')
        if "'" in line[3:5]: #如果有带 " ' "号的
            right_size.append(len(line[7:]))
            right.append(line[7:])
            LR0.append(line[3:4] + ":" + line[7:])
        else: # 正常的
            right_size.append(len(line[6:]))
            right.append(line[6:])
            LR0.append(line[3:4] + ":" + line[6:])


def analysis_LR0(table, LR0, right_size, right, str, analysis_table):
    i = 1 #这个是运行步骤
    symbol_stack = ['#'] #符号栈，初始栈开始就是#
    stra = str[::-1] #将输入的字符倒序，主要是好删除
    status_stack = ['0'] #状态栈，开始是0
    status = True #循环状态
    while status:
        a = [] #这个就是总表中的每个字段
        a.append(i)
        init = ""
        for n_b in status_stack:  #遍历状态
            init += n_b
        a.append(init)

        init = ""
        for single in symbol_stack: #遍历字符栈
            init += single
        a.append(init)

        init = ""
        init = stra[::-1] #当前输入字符
        a.append(init)

        char1 = status_stack[len(status_stack) - 1] #状态栈栈顶
        char2 = stra[len(stra) - 1] #当前输入串栈顶
        if table.get(char1) and table.get(char1).get(char2) is not None: #判断分析表中当前字段是否为空
            sg = table.get(char1).get(char2)
            if sg[0] == 'S': #判断当前字段的首地址S则为移进
                status_stack.append(sg[1:len(sg)])
                symbol_stack.append(char2)
                stra = stra[:-1]
                a.append(sg)
                a.append('   ')
            elif sg[0] == 'r': #r则为规约
                a.append(sg)
                num = right_size[int(sg[1:len(sg)])] #需要判断r后面字符指的是哪条文法，且文法右部的大小，这里需要读取大小表内
                k = num
                while k > 0: #大小多少就出栈多少个
                    status_stack.pop()
                    symbol_stack.pop()
                    k -= 1
                char3 = status_stack[len(status_stack) - 1] #在求当前状态栈顶
                char4 = LR0[int(sg[1:len(sg)])][0] #出栈后的输入串栈顶
                if table.get(char3) and table.get(char3).get(char4) is not None:
                    sg2 = table.get(char3).get(char4)
                    if not sg2.isdigit(): #如果不是数字就报错
                        a.append("报错1")
                        break
                    else: #如果是就加到GOTO字段并入到状态栈顶
                        a.append(sg2)
                        status_stack.append(sg2)
                        symbol_stack.append(char4)
            elif sg == 'acc':
                a.append('acc')
                a.append("   ")
                analysis_table.append(a)
                break
            else:
                a.append('报错2')
                a.append("   ")
                analysis_table.append(a)
                break
        else:
            a.append('报错3')
            a.append("   ")
            analysis_table.append(a)
            break
        i += 1
        analysis_table.append(a)


if __name__ == '__main__':
    table = table() #导入LR0的分析表
    right_size = [] #计算LR0文法的右部的长度
    right = [] #右部的字符串
    LR0 = []  #LR分析总表输出形式是{右部:左部}
    analysis_table = [] #这个是分析过程的总表
    str = input("请输入字符串:")
    # str = "bccd#"
    if not str.endswith("#"):
        str += '#'
    consist(table, LR0, right_size, right) #计算以上除了总表的表
    # print(LR0)
    # print(right)
    # print(right_size)
    analysis_LR0(table, LR0, right_size, right, str, analysis_table) #计算分析过程并加到总表中去
    table_LR0_analysis = PrettyTable()
    table_LR0_analysis.field_names = ["步骤 ", " 状态栈 ", " 符号栈 ", " 当前输入 ", " ACTION ", " GOTO "]
    for row in analysis_table:
        table_LR0_analysis.add_row(row)
    print(table_LR0_analysis)
