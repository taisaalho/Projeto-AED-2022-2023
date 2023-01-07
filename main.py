from calendar import c
from ipaddress import collapse_addresses
from tkinter import *
from tkinter import messagebox
from turtle import width
from PIL import ImageTk, Image
import os.path

if not os.path.isfile('./data/users.txt'):
    file = open('./data/users.txt', mode='w+', encoding="utf-8")
    file.writelines(['João',';','admin',';','admin123',';','admin'])
    file.write("\n")
    file.close()


if not os.path.isfile('./data/categories.txt'):
    file = open('categories.txt', mode='w+', encoding="utf-8")
    file.close()

if not os.path.isfile('./data/games.txt'):
    file = open('./data/games.txt', mode='w+', encoding="utf-8")
    file.close()

if not os.path.isfile('./data/views.txt'):
    file = open('./data/views.txt', mode='w+', encoding="utf-8")
    file.close()

window = Tk()
window.title("GamePick")  #Nome da Aplicação
window.resizable(0,0)
window.iconbitmap("./assets/design.png") #Não dá,não sei porquê
window.configure(bg = "NavajoWhite2") 

#Tamanho e localização da Window
windowHeight = 600
windowWidth = 1000

screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()

x = int((screenWidth/2) - (windowWidth/2))
y = int((screenHeight/2) - (windowHeight/2))

window.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, x, y))

def nav():
    barraNav = Menu(window)
    barraNav.add_command(label = "Home", command = "")
    barraNav.add_command(label = "Games", command = "")
    barraNav.add_command(label = "User", command = "")
    barraNav.add_command(label = "Notifications", command = "")
    barraNav.add_command(label = "Quit", command = "window.quit")
    window.configure(menu = barraNav)

def home():
    nav()
    #Barra de Nome
    framePesquisa = Frame(window,width=1000,height=50,bg="grey")
    framePesquisa.place(x = 0,y = 0)

    #Nome
    lblName = Label(framePesquisa,text = "GamePick",font = ("Saab",25),bg="grey")
    lblName.place(x = 50 , y = 5)

    #Pesquisa
    lblPesquisa = Label(framePesquisa,text = "Pesquisa",font = ("Arial",12))
    lblPesquisa.place(x = 600, y = 15)

    txtPesquisa = Entry(window,width=25)
    txtPesquisa.place(x = 260,y = 77)

    #Jogo Destaque
    panelJogoDestaque = PanedWindow(window,width=600,height=350)
    panelJogoDestaque.place(x = 50, y = 140)

    imagemDestaque = Canvas(panelJogoDestaque,width=400,height=150,relief="sunken")
    imagemDestaque.place(x = 10,y=220)

    """ img = Image(file="assets\SickBoy - AVENTURA.jpg") #Não dá
    image_types.create_image(253, 375, image=img) """

    #Lista de Jogos
    panelListaJogos = PanedWindow(window,width=250,height=350)
    panelListaJogos.place(x = 700, y = 140)


def logout():
    MsgBox = messagebox.askquestion ('Exit Application','Deseja mesmo efetuar o logout?',icon = 'warning')    
    if MsgBox == 'yes':
        """ user_btn.config(text="Login/Registo", command=openWindow)
        user_name.config(text="") """
    else:
        messagebox.showinfo('Return','Vai retornar ao ecrã da aplicação!')    
            
home()  
window.mainloop()