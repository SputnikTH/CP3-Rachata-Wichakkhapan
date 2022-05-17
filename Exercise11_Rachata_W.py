number = int(input("Number : "))
for x in range(number):
    text = ""
    for y in range(2*(x)+1):
        text=text+("*")
    print(" " * (number - x), text)