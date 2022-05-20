menuList = []
def showBill():
    sum = 0
    print(("---My Food---"))
    for number in range(len(menuList)):
        print(menuList[number])
        sum += int(menuList[number][1])
        print("Total :", sum)
while True:
    menuName = input("Please Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price :")
        menuList.append([menuName,menuPrice])
showBill()