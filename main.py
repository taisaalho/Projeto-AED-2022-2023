from calendar import c
from tkinter import ttk 
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





def userProfile():
    return


def loginOrRegister():
    def register():
        check_counter=0
        warn = ""
        data = []
        with open('./data/users.txt',mode='r+', encoding="utf-8")as file:
            for line in file:
                data = line.strip().split(';')  
        if  len(data) > 0 and txtEmail.get() == data[1]:
            warn = "Email já existe!"
        else:
            check_counter += 1
        if txtRepeatPassword.get() == "":
            warn = "Confirmar password não pode estar vazia!"
        else:
            check_counter += 1

        if txtPassword.get() == "":
            warn = "Password não pode estar vazia!"
        else:
            check_counter += 1

        if txtEmail.get() == "":
            warn = "Email não pode estar vazio!"
        else:
            check_counter += 1

        if txtUsername.get() == "":
            warn = "Nome não pode estar vazio!"
        else:
            check_counter += 1

        if txtPassword.get() != txtRepeatPassword.get():
            warn = "Passwords não coicidem!"
        else:
            check_counter += 1

        if check_counter == 6:        
            try:
                user = [txtUsername.get()+';', txtEmail.get()+';',  txtPassword.get()+';','user']
                file = open('./data/users.txt', "a", encoding="utf-8")
                file.writelines(user)
                file.write("\n")
                file.close()
                messagebox.showinfo('confirmation', 'Registo efetuado com sucesso!')
                
                
                #What to do next?#
                    
            except Exception as ep:
                
                messagebox.showerror('Erro!', ep) 
                

        else:
            
            messagebox.showerror('Erro!', warn)
    #Sign In
    frameSignIn = LabelFrame(window, text = "Sign In",width = 460, height = 500, font = ("Arial",10))
    frameSignIn.place(x = 20 , y = 40)

    lblUsernameSignIn = Label(frameSignIn, text = "Username:", font = ("Arial",12))
    lblEmailSignIn = Label(frameSignIn,text = "Email:", font = ("Arial",12))
    lblPasswordSignIn = Label(frameSignIn,text = "Password:", font = ("Arial",12))
    lblRepeatPasswordSignIn = Label(frameSignIn,text = "Repeat Password:", font = ("Arial",12))
    lblUsernameSignIn.place(x = 50, y = 60)
    lblEmailSignIn.place(x = 50, y = 110)
    lblPasswordSignIn.place(x = 50, y = 160)
    lblRepeatPasswordSignIn.place(x = 50,y= 210)

    txtUsername = Entry(frameSignIn,width = 30)
    txtEmail = Entry(frameSignIn,width = 30)
    txtPassword = Entry(frameSignIn,width = 30)
    txtRepeatPassword = Entry(frameSignIn,width = 30)
    txtUsername.place(x = 150, y = 62)
    txtEmail.place(x = 150, y = 112) 
    txtPassword.place(x = 150, y = 162)
    txtRepeatPassword.place(x = 210, y = 212)

    btnConfirmSignIn = Button(frameSignIn,text = "Confirm", font = ("Arial Bold",12), width = 8 ,height = 2,command=register)
    btnConfirmSignIn.place(x = 180,y = 360)


    def login():
        uname = txtUsernameLogin.get()
        upwd = txtPasswordLogin.get()
        check_counter=0
        try:
            with open('./data/users.txt',mode='r+', encoding="utf-8")as file:
                for line in file:
                    data = line.strip().split(';')  
                    if  len(data) > 0 and uname == data[0]:
                        username = data[0]
                        pwd = data[2]
                        check_counter += 1
                    else:
                        warn = "Username não existe!"
        except Exception as ep:
            messagebox.showerror('Erro!', ep)
        if upwd == "":
            warn = "Password não pode estar vazia!"
        else:
            check_counter += 1
        if uname == "":
            warn = "Email não pode estar vazio!"
        else:
            check_counter += 1
        if check_counter == 3:
            if (uname == username and upwd == pwd):
                messagebox.showinfo('Login Status', 'Efetuado login com sucesso!')      
                
                
                home()
                
                
            else:
                messagebox.showerror('Login Status', 'Email ou password inválido(s)!')
        else:
            messagebox.showerror('Erro!', warn)
   


    #Log In
    frameLogIn = LabelFrame(window, text = "Log In",width = 460, height = 500, font = ("Arial",10))
    frameLogIn.place(x = 520, y = 40)

    lblUsername = Label(frameLogIn, text = "Username:", font = ("Arial",12))
    lblPassword = Label(frameLogIn,text = "Password:", font = ("Arial",12))
    lblUsername.place(x = 50, y = 60)
    lblPassword.place(x = 50, y = 98)

    txtUsernameLogin = Entry(frameLogIn,width = 30)
    txtPasswordLogin = Entry(frameLogIn,width = 30)
    txtUsernameLogin.place(x = 150, y = 62)
    txtPasswordLogin.place(x = 150, y = 100)

    btnConfirmLogIn = Button(frameLogIn,text = "Confirm", font = ("Arial Bold",12), width = 8 ,height = 2, command=login)
    btnConfirmLogIn.place(x = 180,y = 150)




def home():
    
    window.withdraw()
    top = Toplevel()
    top.resizable(0,0)
    top.iconbitmap("./assets/design.png") #Não dá,não sei porquê
    top.configure(bg = "NavajoWhite2") 
    top.title("fds")
    barraNav = Menu(top)
    barraNav.add_command(label = "Home", command = "")
    barraNav.add_command(label = "Games", command = userProfile)
    barraNav.add_command(label = "User", command = "")
    barraNav.add_command(label = "Notifications", command = "")
    barraNav.add_command(label = "Quit", command = "window.quit")
    top.configure(menu = barraNav)

    #Barra de Nome
    framePesquisa = Frame(top,width=1000,height=50,bg="grey")
    framePesquisa.place(x = 0,y = 0)

    #Nome
    lblName = Label(framePesquisa,text = "GamePick",font = ("Saab",25),bg="grey")
    lblName.place(x = 50 , y = 5)

    #Pesquisa
    lblPesquisa = Label(framePesquisa,text = "Pesquisa",font = ("Arial",12))
    lblPesquisa.place(x = 600, y = 15)

    txtPesquisa = Entry(top,width=40)
    txtPesquisa.place(x = 700,y= 17)


    x = int((screenWidth/2) - (windowWidth/2))
    y = int((screenHeight/2) - (windowHeight/2))

    top.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, x, y))

  

    #Jogo Destaque
    panelJogoDestaque2 = PanedWindow(top,width=600,height=350)
    panelJogoDestaque2.place(x = 50, y = 140)


    """ img = Image(file="assets\SickBoy - AVENTURA.jpg") #Não dá
    image_types.create_image(253, 375, image=img) """

    #Lista de Jogos
    panelGamesList = PanedWindow(top,width=250,height=350)
    panelGamesList.place(x = 700, y = 140)
    gamesList = Listbox(panelGamesList, width=20)
    with open('./data/games.txt',mode='r+', encoding="utf-8")as file:
                for line in file:
                    data1 = line.strip().split(';')
                    print (data1)
                    gamesList.insert(END, data1[0])                          
    gamesList.place(x=100,y=100)
            
    



def logout():
    MsgBox = messagebox.askquestion('Exit Application','Deseja mesmo efetuar o logout?',icon = 'warning')    
    if MsgBox == 'yes':
        """ user_btn.config(text="Login/Registo", command=openWindow)
        user_name.config(text="") """
    else:
        messagebox.showinfo('Return','Vai retornar ao ecrã da aplicação!')    
            
loginOrRegister()  
window.mainloop()