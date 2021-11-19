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
choosen_symbol = input("Please Choose another operation: ")
function_operation = operations[choosen_symbol]
first_answer = function_operation(num1, num2)
print("{} {} {} ={}".format(num1, choosen_symbol, num2, first_answer))
continue_operation = True
while continue_operation:
  continue_calculation = input("Type 'Y' to continue calculating with {}, or 'N' to exit: ".format(first_answer)).lower()
  if continue_calculation == "y":
    choosen_symbol = input("Please choose another operation: ")
    num3 = int(input("What is the next number?: "))
    function_operation = operations[choosen_symbol]
    second_answer = function_operation(first_answer, num3)
    print("{} {} {} = {}".format(first_answer, choosen_symbol, num3, second_answer))
  else:
      continue_operation = False
      print("Goodbye")