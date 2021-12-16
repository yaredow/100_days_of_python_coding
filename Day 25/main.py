import csv

with open("weather_data.csv") as weather_data:
    data = csv.reader(weather_data)
    temperature = []
    for row in data:
        if row[1] != 'temp':
            temp_new = row[1]
            temperature.append(int(temp_new))
    print(temperature)
