try:
    file = open("a_text")
except FileNotFoundError:
    file = open("a_text", mode="w")
else:
    content = file.read()
    print(content)
finally:
    file.close()
