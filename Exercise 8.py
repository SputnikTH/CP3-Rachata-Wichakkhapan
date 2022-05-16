username = input("Username :")
password = input("password :")
if username == "customer" and password == "shopping1234":
    print("let shopping!")
    print("banana",10,"THB")
    print("milk",5,"THB")
    print("beer",20,"THB")
    print("let choose menu and press order","press paid when you complete")

    userSelected = input(">>")
    if userSelected == "order":
       order1 = input("First Product : ")
       order2 = input("Second Product : ")
       order3 = input("Third Prodect :")
       print(order1,order2,order3)
    elif userSelected == "paid":
        price1 = int(input("First Product Price : "))
        price2 = int(input("Second Product Price : "))
        price3 = int(input("Third Product Price : "))
        print(int(price1+price2+price3),"THB")
else:
    print("retry login")
