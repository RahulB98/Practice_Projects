def add(array):
    sum = float(0)
    for num in array:
        sum += num
    return sum

def product(array):
    pro = float(1)
    for num in array:
        pro *= num
    return(pro)

def subtract(array):
    diff = array[0]
    for num in array[1:]:
        diff -= num
    return diff

def div(a,b):
    return float(a/b)

def line():
    print("\n" + "*"*100)

line()
print("Welcome to calculator!!\nInput the symbol corresponding to the operation you wish to perform\n ")
print("""1.Addition '+'
2.Subtraction '-'
3.Multiplication '*'
4.Division '/'""")

operation = input("Enter: ")
if operation == '+':
    array = []
    print("enter the number of numbers you wish to add")
    n = int(input("Enter :"))
    print("now enter the numbers!")
    for i in range(n):
        num = int(input("Enter :"))
        array.append(num)
    print(add(array))
elif operation == '-':
    array = []
    print("enter the number of numbers you wish to add")
    n = int(input("Enter :"))
    print("now enter the numbers!")
    for i in range(n):
        num = int(input("Enter :"))
        array.append(num)
    print(subtract(array))
elif operation == '*':
    array = []
    print("enter the number of numbers you wish to add")
    n = int(input("Enter :"))
    print("now enter the numbers!")
    for i in range(n):
        num = int(input("Enter :"))
        array.append(num)
    print(product(array))
elif operation == '/':
    a = input("Numerator: ")
    b = input("Denominator: ")
    print(div(int(a), int(b)))
else:
    print("Please chosse a proper operator!")