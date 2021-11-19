from art import logo 
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
def calculator():
  print(logo) 
  num1 = int(input("What is the first number?: "))
  for symbol in operations:
      print(symbol)
  continue_operation = True
  while continue_operation:
    choosen_symbol = input("Please Choose operation: ")
    num2 = int(input("What is the second number?: "))
    function_operation = operations[choosen_symbol]
    answer = function_operation(num1, num2)
    print("{} {} {} ={}".format(num1, choosen_symbol, num2, answer))

    continue_calculation = input("Type 'Y' to continue calculating with {}, or 'N' to exit: ".format(answer)).lower()
    if continue_calculation == "y":
      num1 = answer
    else:
      continue_operation = False
      calculator()
calculator()    
