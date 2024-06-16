# # list 1
# # task 1
# string1 = ' Ala '
# string2 = '''12213
# wiele lini'''
# int1 = 1
# int2 = -234
# float1 = 1.2
# float2 = -123.1213
#
# print(string1, string2, int1, int2, float1, float2)

# task 2
try:
    x = float(input("Insert X value: "))
    operator = input("Insert math operator: ")
    y = float(input("Insert Y value: "))
    while operator != '*' and operator != '/' and operator != '-' and operator != '+':
        print("Invalid operator.")
        operator = input("Insert operator from the list: \"+ , - , * , / \": ")
    if operator == '/':
        print(x / y)
    elif operator == '*':
        print(x * y)
    elif operator == '+':
        print(x + y)
    elif operator == '-':
        print(x - y)
except ValueError:
    print("Unable to convert input value to floating-point number")

# task 3 list
# task 4 dict
# task 5 files