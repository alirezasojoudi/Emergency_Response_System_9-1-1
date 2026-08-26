from tkinter import *
from project.view.emergency_form import emergency_window
from PIL import Image, ImageTk

win = Tk()
win.geometry("600x250")
win.title("9.1.1 Operator")

win.resizable(width=False, height=False)
win.configure(bg="gray22")

img = Image.open("D:/python 3710/project/view/icon_picture/police.png")
img = img.resize((130, 130))
img = ImageTk.PhotoImage(img)

img1 = Image.open("D:/python 3710/project/view/icon_picture/ambulance.png")
img1 = img1.resize((130, 130))
img1 = ImageTk.PhotoImage(img1)

img2 = Image.open("D:/python 3710/project/view/icon_picture/fire.png")
img2 = img2.resize((130, 130))
img2 = ImageTk.PhotoImage(img2)

Label(win, text="EMERGENCY RESPONSE SYSTEM", bg="gray22", fg="white", font=("Helvetica", 20, "bold")).place(x=65, y=5)
Label(win, text="Police", bg="gray22", fg="white", font=("Helvetica", 14, "bold")).place(x=75, y=60)
Label(win, text="Ambulance", bg="gray22", fg="white", font=("Helvetica", 14, "bold")).place(x=245, y=60)
Label(win, text="Fire station", bg="gray22", fg="white", font=("Helvetica", 14, "bold")).place(x=440, y=60)

Button(win, borderwidth=7, background="white",command=lambda: emergency_window("Police 🚨"), activebackground="royal blue1", image=img).place(x=25, y=85, width=150,height=100)
Button(win, borderwidth=7, background="white",command=lambda: emergency_window("Ambulance⚕️"), activebackground="deepskyblue3", image=img1).place(x=225, y=85,width=150, height=100)
Button(win, borderwidth=7, background="white",command=lambda: emergency_window("Fire Station 🚒"), activebackground="firebrick1", image=img2).place(x=425, y=85, width=150,height=100)

