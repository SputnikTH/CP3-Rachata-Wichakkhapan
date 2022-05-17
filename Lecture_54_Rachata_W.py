def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return showMenu()
    else:
        return login()
def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    return menuSelect()
def menuSelect():
    userSelected = int(input(">>"))
    if userSelected == 1 :
        return vatCalculate()
    elif userSelected == 2 :
        return priceCalculate()
    else:
        return menuSelect()
def vatCalculate():
    vat = 7
    totalPrice = int(input("price : "))
    result = totalPrice + (totalPrice * vat / 100)
    return result
    print(vatCalculate())
def priceCalculate():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    totalPrice = price1+price2
    return totalresult(totalPrice)
    print(priceCalculate())
def totalresult(totalPrice):
    vat = 7
    result = totalPrice + int(totalPrice * vat / 100)
    return result
print(login())
