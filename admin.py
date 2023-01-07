from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
""" from tkvideo import tkvideo """
from tkinter import ttk
from tkinter import messagebox


#Funções









#window
window = Tk()
window.title("GamePick")  #Nome da Aplicação
window.resizable(0,0)
window.iconbitmap("assets\\transferir.png") #Não dá,não sei porquê
window.configure(bg = "NavajoWhite2") 

#Tamanho e localização da Window
windowHeight = 600
windowWidth = 1000

screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()

x = int((screenWidth/2) - (windowWidth/2))
y = int((screenHeight/2) - (windowHeight/2))

window.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, x, y))


#Design e Funcionalidades

#Barra de Navegação
barraNav = Menu(window)
barraNav.add_command(label = "Home", command = "")
barraNav.add_command(label = "Games", command = "")
barraNav.add_command(label = "User", command = "")
barraNav.add_command(label = "Notifications", command = "")
barraNav.add_command(label = "Quit", command = "window.quit")

window.configure(menu = barraNav)

#Barra de Nome
framePesquisa = Frame(window,width=1000,height=50,bg="grey")
framePesquisa.place(x = 0,y = 0)

#Nome
lblName = Label(framePesquisa,text = "GamePick",font = ("Saab",25),bg="grey")
lblName.place(x = 440, y = 5)

#Pesquisa
lblPesquisa = Label(window,text = "Pesquisa",font = ("Arial",12))
lblPesquisa.place(x = 160, y = 75)

txtPesquisa = Entry(window,width=100)
txtPesquisa.place(x = 260,y = 77)

#Jogo Destaque
panelJogoDestaque = PanedWindow(window,width=600,height=350)
panelJogoDestaque.place(x = 50, y = 140)

imagemDestaque = Canvas(panelJogoDestaque,width=400,height=150,relief="sunken")
imagemDestaque.place(x = 10,y=220)

""" img = Image(file="assets\SickBoy - AVENTURA.jpg") """ #Não dá
""" image_types.create_image(253, 375, image=img) """

#Lista de Jogos
panelListaJogos = PanedWindow(window,width=250,height=350)
panelListaJogos.place(x = 700, y = 140)















window.mainloop()