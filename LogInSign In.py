from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
from tkvideo import tkvideo
from tkinter import ttk
from tkinter import messagebox


#Window
window = Tk()
window.title("GamePick")  #Nome da Aplicação
window.resizable(0,0)
window.iconbitmap("assets\\Design sem nome.png") #Não dá,não sei porquê
window.configure(bg = "NavajoWhite2") 

#Tamanho e localização da Window
windowHeight = 600
windowWidth = 1000

screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()

x = int((screenWidth/2) - (windowWidth/2))
y = int((screenHeight/2) - (windowHeight/2))

window.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, x, y))


#Design/Funcionalidades

#Sign In
frameSignIn = LabelFrame(window, text = "Sign In",width = 460, height = 500, font = ("Arial",10))
frameSignIn.place(x = 20 , y = 40)

lblUsername = Label(frameSignIn, text = "Username:", font = ("Arial",12))
lblEmail = Label(frameSignIn,text = "Email:", font = ("Arial",12))
lblPassword = Label(frameSignIn,text = "Password:", font = ("Arial",12))
lblRepeatPassword = Label(frameSignIn,text = "Repeat Password:", font = ("Arial",12))
lblUsername.place(x = 50, y = 60)
lblEmail.place(x = 50, y = 110)
lblPassword.place(x = 50, y = 160)
lblRepeatPassword.place(x = 50,y= 210)

txtUsername = Entry(frameSignIn,width = 30)
txtEmail = Entry(frameSignIn,width = 30)
txtPassword = Entry(frameSignIn,width = 30)
txtRepeatPassword = Entry(frameSignIn,width = 30)
txtUsername.place(x = 150, y = 62)
txtEmail.place(x = 150, y = 112) 
txtPassword.place(x = 150, y = 162)
txtRepeatPassword.place(x = 210, y = 212)

btnConfirmSignIn = Button(frameSignIn,text = "Confirm", font = ("Arial Bold",12), width = 8 ,height = 2)
btnConfirmSignIn.place(x = 180,y = 360)


#Log In
frameLogIn = LabelFrame(window, text = "Log In",width = 460, height = 500, font = ("Arial",10))
frameLogIn.place(x = 520, y = 40)

lblUsername = Label(frameLogIn, text = "Username:", font = ("Arial",12))
lblPassword = Label(frameLogIn,text = "Password:", font = ("Arial",12))
lblUsername.place(x = 50, y = 60)
lblPassword.place(x = 50, y = 160)

txtUsername = Entry(frameLogIn,width = 30)
txtPassword = Entry(frameLogIn,width = 30)
txtUsername.place(x = 150, y = 62)
txtPassword.place(x = 150, y = 162)

btnConfirmLogIn = Button(frameLogIn,text = "Confirm", font = ("Arial Bold",12), width = 8 ,height = 2)
btnConfirmLogIn.place(x = 180,y = 360)


















window.mainloop()