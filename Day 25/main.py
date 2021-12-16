import pandas

squirrel_color = pandas.read_csv("4.1 2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
Gray_squirrel = squirrel_color[squirrel_color["Primary Fur Color"] == "Gray"]
Black_squirrel = squirrel_color[squirrel_color["Primary Fur Color"] == "Black"]
Cinnamon_squirrel = squirrel_color[squirrel_color["Primary Fur Color"] == "Cinnamon"]

# identifying the number of each squirrels
num_gray_squirrels = len(Gray_squirrel)
print(num_gray_squirrels)
num_black_squirrels = len(Black_squirrel)
print(num_black_squirrels)
num_cinnamon_squirrels = len(Cinnamon_squirrel)
print(num_cinnamon_squirrels)

# constructing dict
num_of_squirrels = {
    "Color": ["Gray Squirrel", "Black Squirrel", "Cinnamon Squirrel"],
    "Number": [2473, 103, 392]
}

# creating a csv
data_frame = pandas.DataFrame(num_of_squirrels)
data_frame.to_csv("Number of squirrels.csv")
