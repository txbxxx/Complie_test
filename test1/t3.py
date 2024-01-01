# coding=utf-8
"""

================================================================

author: Tan Chang 
file: test1.py.py
date:2023/12/6

================================================================

"""

import re


# 判断变量值的方法
def check_var(s_1, j, ):
    # 判断是否为整形和实型
    if bool(re.match(r'^[-+]?[0-9]', s_1[j])):
        if bool(re.match(r"^(\+?-?\d+)$", s_1[j][1:])):
            print(s_1[j] + "为合法变量且是整形")
            return 'int_num'
        if bool(re.match(r'^[0-9]?[Ee][+-]?[0-9]+$', s_1[j][1:])):
            print(s_1[j] + "为合法变量且是整形")
            return 'int_num'
        if bool(re.match(r"^(\+?-?\d+(\.\d+)?|0(\.\d+)?)$", s_1[j])):
            print(s_1[j] + "为合法变量且是实型")
            return 'real_num'
    if bool(re.match(r'^".*"$', s_1[j])):
        print(s_1[j] + "为合法变量且是字符串")
        return 'str_num'
    if bool(re.match(r"^'.?'$", s_1[j])):
        if len(s_1[j][1:-1]) > 1:
            print(s_1[j] + "它不是一个单个字符")
            return 'break'
        else:
            print(s_1[j] + "它是一个单个字符")
            return 'str_num'
    else:
        print(s_1[j] + "为不合法变量")
        return "break"


# 判断变量名的方法
def check_varname(s_1, j, str_list, i):
    # 删除空格
    # 判断变量名是否出现重复
    x = 1
    while x < i:
        if i >= 2:
            s_2 = str_list[x].split("=")
            if s_1[j] == s_2[j]:
                print(s_1[j] + "变量名已经存在于第" + str(x) + "个")
                return "break"
            else:
                x += 1
    if i >= 1:
        if not s_1[j][0].isalpha():
            print(s_1[j] + "不合法")
            return "break"
        elif len(s_1[j]) >= 2:
            # print(s_1[j][1:])
            # if not bool(re.match(r'^[a-zA-Z]+[0-9]+_+', s_1[j][1:])):
            if not bool(re.match(r'^[a-zA-Z][a-zA-Z0-9_]*$', s_1[j][1:])):
                print(s_1[j] + "的" + s_1[j][1:] + "不合法")
                return "break"
            else:
                print(s_1[j] + "为合法变量名")


# 在此处判断变量和变量名
def check_varname_var(str_list, j, i):
    # 判断后面句子有 “=”号，再去匹配“=”前和后
    if bool(str_list[i].find("=")):
        print()
        # 将 “=”前后字符放入列表中
        s_1 = str_list[i].split("=", 1)
        print(s_1)
        # 判断是否有多余的
        if len(s_1) > 2:
            print(str_list[i] + "不合法")
            return "break"
        elif len(s_1) == 1:
            print("变量名" + s_1[0] + "未被赋值")
            return "break"
        # print(s_1[1])
        while j < len(s_1):
            s_1[j].split()
            # 判断变量名
            if j == 0:
                if check_varname(s_1, j, str_list, i) == "break":
                    return "break"
            # 判断变量值
            elif j == 1:
                num = check_var(s_1, j, )
                if num == 'int_num':
                    return "int_num"
                if num == 'str_num':
                    return "str_num"
                if num == 'real_num':
                    return "real_num"
            j += 1


# 检查语法开头
def check_const(i, str_list):
    if str_list[i] == 'const':
        print(str_list[i] + "为合法变量说明语句内容")
        return "continue"
    elif str_list[0] != 'const':
        print(str_list[0] + "不合法")
        return "break"

#检查输入
def check_input(strl):
    #输入quit或者exit就退出
    if strl == "quit" or strl == "exit":
        print("退出程序")
        return False

    #创建1分割列表
    str_list = []

    ##判断字符串开始是否为const
    if strl.startswith('const'):
        str_list.append('const')
        ##如果为const就将const和它后面的一个空隔去除
        strl = strl[6:].strip()
    else:
        print("输入错误，未以const开头")
        return 'continue'
    pattern = r'"[^"]*"|\w+\s*=\s*"(?:\\.|[^"\\])*"|\w+\s*=\s*[^,;]+'
    code_blocks = re.findall(pattern, strl)
    print(code_blocks)
    #遍历列表
    for i, code in enumerate(code_blocks):
        #检查字符串中是否包含;和双引号是否为奇数
        if ';' in code and code.count('"') % 2 != 0:
            #去除分号
            code = code.split(';')[0]
            str_list.append(code.strip())
            str_list.append(';')
            break
        #判断字符是是不是以,号结尾
        if code.endswith(","):
            #下一个元素地址
            next_code_index = i + 1
            while next_code_index < len(code_blocks) and code_blocks[next_code_index].endswith(","):
                code += code_blocks[next_code_index]
                next_code_index += 1
                str_list.append(code)
        else:
            str_list.append(code.strip())
    if strl.endswith(";"):
        str_list.append(";")
    else:
        print("结尾符号错误：" + " 应该为';'")
        return 'continue'
    for i in range(1, len(str_list)):
        if bool(re.match(r'^\s*$', str_list[1])):
            print("输入的变量和变量名不合法")
            # return 'continue'
    for i in range(1, len(str_list) - 1):
        # 判断变量名是否合法
        if not re.match(r'^[a-zA-Z_][\w.]*$', str_list[i].split('=')[0].strip()):
            print("输入的变量名不合法：" + str_list[i].split('=')[0].strip())
            str_list.insert(i, str_list[i].split('=')[0].strip() + '=')
            return 'continue'
        str_list[i] = str_list[i].replace('=', '=').strip()

        # 去除变量名后的空格        str_list[i] = str_list[i].split('=')[0].strip() + '=' + str_list[i].split('=')[1].strip()
    print("分割后的列表为：")
    print(str_list)

    return str_list


def start_program():
    status = True
    while status:
        #
        int_num = 0
        #
        str_num = 0
        #
        real_num = 0
        # =号拆分数组的循环变量
        j = 0
        # 主题列表的循环变量
        str1 = input("请输入: ")
        # 删除前后空格
        strl = str1.strip()
        str_list = check_input(strl)
        if not str_list:
            status = str_list
        elif str_list == 'continue':
            continue
        else:
            for i in range(len(str_list)):
                # for i in enumerate(str_list):
                # 判断句子开始是否为’const‘,是则继续检测下一条，不是则退出并输出不合法
                const_s = check_const(i, str_list)
                if const_s == "break":
                    break
                elif const_s == "continue":
                    continue
                if i >= 1:
                    if str_list[i] == str_list[-1]:
                        if str_list[i] == ";":
                            print("语句匹配结束")
                            print("该语句的整形变量、字符型变量、实型变量分别有：" + str(int_num) + "、" + str(str_num) + "、" + str(real_num))
                            break
                        else:
                            print("语句结束语句结尾符号错误")
                    else:
                        num = check_varname_var(str_list, j, i)
                        if num == 'int_num':
                            int_num += 1
                        elif num == 'str_num':
                            str_num += 1
                        elif num == 'real_num':
                            real_num += 1
                        elif num == 'break':
                            break

                else:
                    print("没有变量被定义！！")


start_program()
