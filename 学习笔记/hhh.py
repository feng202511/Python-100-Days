# This is a test file.

print("Hello, world!")

# This is a test file.

# This is a test file.

# This is a test file.
# 一个计算器的程序

# 导入必要的模块
import math

# 定义计算器函数
def calculator():   
    
    # 输入两个数字
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))                

    # 选择运算符        
    operator = input("Enter the operator (+, -, *, /): ")

    # 进行运算
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Error: division by zero")
            return
        else:
            result = num1 / num2
    else:
        print("Error: invalid operator")
        return

    # 输出结果
    print("Result: ", result)

# 调用计算器函数
calculator()

