def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mul(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2
operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}
num1 = int(input("What is the first number?: "))
num2 = int(input("What is the second number?: "))
for symbol in operations:
    print(symbol)
choosen_symbol = input("Please Choose an operation: ")
if choosen_symbol == "+":
    print("{} {} {} = {}".format(num1, choosen_symbol, num2,  add(num1, num2)))
elif choosen_symbol == "-":
    print("{} {} {} = {}".format(num1, choosen_symbol, num2,  sub(num1, num2)))
elif choosen_symbol == "*":
    print("{} {} {} = {}".format(num1, choosen_symbol, num2,  mul(num1, num2)))
elif choosen_symbol == "/":
    print("{} {} {} = {}".format(num1, choosen_symbol, num2,  div(num1, num2)))
else:
    print("Invalid input!")
