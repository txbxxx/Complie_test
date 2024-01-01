import re

def swap(strs):
    str2 = strs.group(1).replace('=', '0xWs')
    return str2 + strs.group(3)


def swap_a(strs):
    # 将=替换为0xWs
    str2 = strs.group(1).replace('0xWs', '=')
    return str2 + strs.group(3)


def swap_black(strs):
    # 将0xWs替换为=
    strs = strs.replace('0xWs', '=')
    return strs


def search_string(strs):
    strs = re.sub(r'((["\']).*?\2)([,;])', swap, strs)  # 匹配常量说明语句
    return strs


def search_str():
    input_str = (input("请输入常量说明语句\n"))  # 输入常量说明语句
    input_str = search_string(input_str)  # 匹配常量说明语句
    str1 = [item.strip() for item in re.split(r',(?=(?:[^q\"]*\"[^\"]*\")*[^\"]*$)', input_str)]
    result = (input_str.startswith('const ') and input_str.endswith(';'))
    print(str1)
    if not result:
        print("输入不合法")
        print("It is not a constant declaration statement!")
        print("Please input a string again!")
        return search_str()

    str1[0] = str1[0].replace('const ', '')  # 将const删除
    str1[-1] = str1[-1].replace(';', '')  # 删除尾部的分号
    return str1


def search_name(name):
    return bool(re.match(r'^[a-zA-Z_]\w*$', name))  # 匹配变量名


def search_value(value):
    if re.match(r'^[0-9]+$', value):  # 匹配整数
        return "integer"
    elif re.match(r'^[0-9]?[Ee][+-]?[0-9]+$', value):  # 匹配整数科学计算法
        return "科学计算法"
    elif re.match(r'^[0-9]+\.[0-9]+$|\.+[0-9]+', value):  # 匹配浮点数
        return "float"
    elif re.match(r'^[0-9]?\.[0-9]+[Ee][+-]?[0-9]+$', value):  # 匹配浮点数科学计算法
        return "科学计算法"
    elif re.match(r'^".*"$', value):  # 匹配双引号括起来的字符串
        return "string"
    elif re.match(r"^'.?'$", value):  # 匹配单引号括起来的字符
        return "char"

    else:
        return "unknown"  # 未知类型


if __name__ == '__main__':
    # 统计常量的个数
    int_num = 0
    float_num = 0
    string_num = 0
    char_num = 0
    names = set()
    print("=====================")
    # 输入常量说明语句
    str1 = search_str()
    print(len(str1))
    print("=====================")
    # 遍历str1
    for i in range(len(str1)):
        # 对于只有name或者value的情况
        if str1[i].count('=') != 1:
            print(str1[i] + "不存在赋值情况")
            continue
        # 将name和value分开
        name, value = str1[i].split("=")
        # 如果value没有值那么赋null
        if not value:
            value = "null"
        # 将name存起来，之后判断有无重复的命名
        if name in names:
            print(name + "命名重复")
            continue
        else:
            names.add(name)
        # 将value中的0xWs替换为=
        value = swap_black(value)
        # 判断name和value是否符合规范
        if search_name(name):
            print(name + "命名规范,其数据类型为" + search_value(value) + ",其数据的值为" + value)
            if search_value(value) == "integer":
                int_num += 1
            if search_value(value) == "float":
                float_num += 1
            if search_value(value) == "string":
                string_num += 1
            if search_value(value) == "char":
                char_num += 1
        else:
            print(name + "命名不规范")
    # 输统计常量结果
    print("=====================")
    print('int_num =%d;float_num =%d;string_num =%d;char_num =%d;' % (int_num, float_num, string_num, char_num))
    print("=====================")