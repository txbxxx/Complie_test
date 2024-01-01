import re  # 导入正则表达式模块

# 存放常量名
name = ""
names = set()
# 存放常量值
value = ""
# 存放常量值类型
type = ""
# 存放错误信息
error_info = ""
# 0表示常量名错误，1表示常量名正确
correct_name = 0
# 0表示常量值错误，1表示常量值正确
correct_value = 0
# 用于统计各种类型的常量数量
int_num = 0
string_num = 0
float_num = 0
char_num = 0

flag = 0
# 判断常量名是否合法
def check_name(a, i):
    global name, correct_name, names,flag  # 声明为全局变量
    name = ""
    flag = 0
    while a[i] != '=' and i < len(a) - 1:
        name += a[i]
        i += 1
    name = name.strip()  # 去除字符串前后的空格
    regex = r"[a-zA-Z_][a-zA-Z0-9_]*"  # 用于匹配以字母开头，后跟零个或多个字母、数字或下划线的字符串
    result = re.fullmatch(regex, name)  # 不要用match,要用fullmatch
    if result:
        if name in names:
            correct_name = 0
            flag = 1
        else:
            correct_name = 1  # 常量名合法
            names.add(name)  # 将常量名加入集合
    else:
        correct_name = 0  # 常量名不合法
    return i  # 返回等于号的位置


def check_type(a, i):  # 从等于号的下一个字符开始检查
    global value, error_info, correct_value, type, int_num, string_num, float_num, char_num, correct_name
    value = ""
    error_info = ""
    while a[i] != ',' and a[i] != ';' and i <= len(a) - 1:
        value += a[i]
        i += 1  # 此时i为,或者;的位置
    value = value.strip()
    if correct_name == 1:
        if value.startswith("'"):
            if ((re.fullmatch(r"'.'", value))):
                correct_value = 1
                type = "char"
                char_num += 1
            else:
                error_info += "char类型常量的格式不正确!"
                correct_value = 0
        elif value.startswith("\""):
            if not re.fullmatch(r"\"[\s\S]*\"", value): #\s匹配任何空白字符
                if i < len(a) - 1:
                    value += a[i]
                    i += 1
                    # 一直往后找，直到找到",结尾，字符"和,之间可以有多个空格
                    while i < len(a) and not ((a[i] == ',' or a[i] == ';') and value.strip()[-1] == "\"" ):
                        value += a[i]
                        i += 1
            value = value.strip()
            if (value.endswith("\"")):
                correct_value = 1
                type = "string"
                string_num += 1
            else:
                error_info += "string类型常量的格式不正确!"
                correct_value = 0
        else:

            if (re.fullmatch(r"[+|-]?[0-9]+", value)):
                correct_value = 1
                type = "integer"
                int_num += 1
            # 判断该数是否为浮点数
            elif re.fullmatch(r"[+|-]?[0-9]*?[.][0-9]+", value):
                correct_value = 1
                type = "float"
                float_num += 1
            # 当该数为科学计数法时（小数点前后不能同时没有数字，e，E后面必须要有数字）
            elif (re.fullmatch(r"[+|-]?[0-9]+[.]?[0-9]*?[E|e][+|-]?[0-9]+", value) or re.fullmatch(
                    r"[+|-]?[0-9]*?[.][0-9]+[E|e][+|-]?[0-9]+", value)):
                            correct_value = 1
                            type = "float"
                            float_num += 1
            else:
                error_info += "常量的格式不正确!"
    return i

def output(s):
    global name, correct_name, correct_value, type, value, error_info, int_num, string_num, float_num, char_num,flag
    str_list = list(s)  # 将字符串s转换为字符列表
    i = 5  # 跳过前5个字符const
    while i < len(str_list) - 1:  # 当i=len(str_list)-1时到达末尾字符';'的位置，循环结束
        i = check_name(str_list, i)  # 从const后面一个字符开始检查，返回值为等于号的位置
        # 从等号的下一个字符开始检查并判断数据类型
        i = check_type(str_list, i + 1) + 1  # i+1是为了跳过等号 ,+1是为了跳过逗号
        # 此时i变为,后面一个字符的位置
        # 常量名定义正确，继续判断常量值
        if correct_name == 1:
            # 常量值正确，输出结果，包含常量名，常量类型以及常量值
            if correct_value == 1:
                print(f"{name}({type},{value})")
            # 常量值错误，给出错误类型
            else:
                print(f"{name}({error_info})")
        # 常量名定义错误
        else:
            if(flag==1):
                error_info += "这个变量名已经定义过了!"
            else:
                error_info += "变量名不合法!"
            print(f"{name}({error_info})")
        correct_value= 0 #重新置零

    print(f"int_num={int_num};  char_num={char_num};  string_num={string_num};  float_num={float_num}.")


if __name__ == "__main__":
    # 获取用户输入的字符串
    # strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列
    s = input("请输入一个字符串:\n").strip()
    # 判断字符串是否以“const"开头并且以”；”结尾
    result = s.startswith("const") and s.endswith(";") and s[5] == ' '  # 确保const后面有一个空格，eg:constcount=23;应该为错误的输入
    while not result:
        # 如果输入字符串不是以“const"开头并且以”；”结尾，则输出错误信息，并且要求重新输入
        print("不是合法的常量说明语句!\n")
        s = input("请重新输入一个字符串:\n").strip()
        result = s.startswith("const") and s.endswith(";") and s[5] == ' '
    output(s)



