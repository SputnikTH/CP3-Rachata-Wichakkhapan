menuList = []
priceList = []
def showBill():
    sum = 0
    print(("---My Food---"))
    for number in range(len(menuList)):
        print(menuList[number],priceList[number])
        sum+= int(priceList[number])
        print("Total Price :",sum)
while True:
    menuName = input("Please Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price :")
        menuList.append(menuName)
        priceList.append(menuPrice)
print(menuList,priceList)
showBill()