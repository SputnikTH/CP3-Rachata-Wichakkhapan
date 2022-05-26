from tkinter import *
import math
def leftClickButton(event):
    Bmi = float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2)
    if Bmi >30.0:
        bodyType = "อ้วนมาก"
    if Bmi >= 25.0 and Bmi <= 29.9:
        bodyType = "อ้วน"
    if Bmi >= 23.0 and Bmi <= 24.9:
        bodyType = "น้ำหนักเกิน"
    if Bmi >= 18.6 and Bmi <= 22.9:
        bodyType = "น้ำหนักปกติ เหมาะสม"
    if Bmi <= 18.5:
        bodyType = "ผอมเกินไป"
    lebelResult.configure(text=Bmi)
    lebelbodyType.configure(text=bodyType)

MainWindow = Tk()
lebelHeight = Label(MainWindow,text="ส่วนสูง (CM)")
lebelHeight.grid(row=0,column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)
lebelWeight = Label(MainWindow,text="น้ำหนัก")
lebelWeight.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(MainWindow,text="คำนวณ")
calculateButton.bind('<Button-1>',leftClickButton)
calculateButton.grid(row=2,column=0)
lebelResult = Label(MainWindow,text="ผลลัพธ์")
lebelResult.grid(row=2,column=1)
lebelbodyType = Label(MainWindow,text="รูปร่างของคุณ")
lebelbodyType.grid(row=3,column=1)
MainWindow.mainloop()