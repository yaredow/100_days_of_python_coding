import math
def paint_calc(Height, Width, Cover):
  area = Height * Width
  num_of_cans = math.ceil(area / Cover)
  print(f"You need {num_of_cans} cans of pints")

test_h = int(input("Please insert height of the wall: "))
test_w = int(input("Please insert width of the wall: ") )
coverage = 5
paint_calc(Height=test_h, Width=test_w, Cover=coverage)