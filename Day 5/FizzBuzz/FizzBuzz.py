def fizzbuzz():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("fizzbuzz ", end="")
        elif number % 3 == 0:
            print("buzz ", end="")
        elif number % 5 == 0:
            print("Fizz ", end="")
        else:
            print("{} ".format(number), end="")
fizzbuzz()        

  