import random

def generate_code(code_len=4):
    """
    生成指定长度的验证码

    :param code_len: 验证码的长度(默认4个字符)

    :return: 由大小写英文字母和数字构成的随机验证码
    """
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # 计算 all_chars 列表的最后一个元素的索引
    last_pos = len(all_chars) - 1
    # 此变量用于存储代码字符串
    code = ''
    for _ in range(code_len):
        # 随机生成一个0到last_pos之间的整数
        index = random.randint(0, last_pos)
        # 将字符数组中的特定字符添加到代码字符串中
        code += all_chars[index]
    return code
print(generate_code())
