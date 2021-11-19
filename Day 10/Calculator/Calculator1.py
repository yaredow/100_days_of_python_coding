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
function_operation = operations[choosen_symbol]
first_answer = function_operation(num1, num2)
print("{} {} {} ={}".format(num1, choosen_symbol, num2, function_operation(num1, num2)))