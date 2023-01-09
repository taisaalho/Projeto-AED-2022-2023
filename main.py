from calendar import c
from tkinter import ttk 
from ipaddress import collapse_addresses
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.ttk import Combobox
from turtle import width
from PIL import ImageTk, Image
import os.path


#Funções

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


#LogIn/SignIn Page

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


#Function Pages


def notificationPage():

    notificationPage = Toplevel()
    notificationPage.resizable(0,0)
    notificationPage.iconbitmap("./assets/design.png") #Não dá,não sei porquê
    notificationPage.configure(bg = "NavajoWhite2") 
    notificationPage.title("Notification Page")
   
   #Tamanho e localização da Window
    windowHeight = 600
    windowWidth = 1000

    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()

    x = int((screenWidth/2) - (windowWidth/2))
    y = int((screenHeight/2) - (windowHeight/2))

    notificationPage.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, x, y))

    #Barra de Navegação
    barraNav = Menu(notificationPage)
    barraNav.add_command(label = "Home", command = lambda:[homePage(),notificationPage.destroy()])
    barraNav.add_command(label = "Games", command = lambda:[gamesPage(),notificationPage.destroy()])
    barraNav.add_command(label = "User", command = lambda:[userPage(),notificationPage.destroy()])
    barraNav.add_command(label = "Notifications", command = "")
    barraNav.add_command(label = "Search",command = lambda:[searchPage(),notificationPage.destroy()])
    barraNav.add_command(label = "Quit", command = notificationPage.destroy)

    notificationPage.configure(menu = barraNav)


    #Barra de Nome
    frame1 = Frame(notificationPage,width=1000,height=50,bg="grey")
    frame1.place(x = 0,y = 0)

    #Nome
    lblName = Label(frame1,text = "GamePick",font = ("Saab",25),bg="grey")
    lblName.place(x = 50 , y = 5)

def userPage():
    window.withdraw()
    userPage = Toplevel()
    userPage.resizable(0,0)
    userPage.iconbitmap("./assets/design.png") #Não dá,não sei porquê
    userPage.configure(bg = "NavajoWhite2") 
    userPage.title("User Page")
   
   #Tamanho e localização da Window
    windowHeight = 600
    windowWidth = 1000

    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()

    x = int((screenWidth/2) - (windowWidth/2))
    y = int((screenHeight/2) - (windowHeight/2))

    userPage.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, x, y))

    #Barra de Navegação
    barraNav = Menu(userPage)
    barraNav.add_command(label = "Home", command = lambda:[homePage(),userPage.destroy()])
    barraNav.add_command(label = "Games", command = lambda:[gamesPage(),userPage.destroy()])
    barraNav.add_command(label = "User", command = "")
    barraNav.add_command(label = "Notifications", command = lambda:[notificationPage(),userPage.destroy()])
    barraNav.add_command(label = "Search",command = lambda:[searchPage(),userPage.destroy()])
    barraNav.add_command(label = "Quit", command = userPage.destroy)

    userPage.configure(menu = barraNav)

    #Barra de Nome
    frame1 = Frame(userPage,width=1000,height=50,bg="grey")
    frame1.place(x = 0,y = 0)

    #Nome
    lblName = Label(frame1,text = "GamePick",font = ("Saab",25),bg="grey")
    lblName.place(x = 50 , y = 5)

    #Page 
    

def gamesPage():
    
    gamesPage = Toplevel()
    gamesPage.resizable(0,0)
    gamesPage.iconbitmap("./assets/design.png") #Não dá,não sei porquê
    gamesPage.configure(bg = "NavajoWhite2") 
    gamesPage.title("Games Page")
   
   #Tamanho e localização da Window
    windowHeight = 600
    windowWidth = 1000

    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()

    x = int((screenWidth/2) - (windowWidth/2))
    y = int((screenHeight/2) - (windowHeight/2))

    gamesPage.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, x, y))

    #Barra de Navegação
    barraNav = Menu(gamesPage)
    barraNav.add_command(label = "Home", command = lambda:[homePage(),gamesPage.destroy()])
    barraNav.add_command(label = "Games", command = "")
    barraNav.add_command(label = "User", command = lambda:[userPage(),gamesPage.destroy()])
    barraNav.add_command(label = "Notifications", command = lambda:[notificationPage(),gamesPage.destroy()])
    barraNav.add_command(label = "Search",command = lambda:[searchPage(),gamesPage.destroy()])
    barraNav.add_command(label = "Quit", command = gamesPage.destroy)

    gamesPage.configure(menu = barraNav)

    #Barra de Nome
    frame1 = Frame(gamesPage,width=1000,height=50,bg="grey")
    frame1.place(x = 0,y = 0)

    #Nome
    lblName = Label(frame1,text = "GamePick",font = ("Saab",25),bg="grey")
    lblName.place(x = 50 , y = 5)

def searchPage():
    window.withdraw()
    searchPage = Toplevel()
    searchPage.resizable(0,0)
    searchPage.iconbitmap("./assets/design.png") #Não dá,não sei porquê
    searchPage.configure(bg = "NavajoWhite2") 
    searchPage.title("Search Page")
   
   #Tamanho e localização da Window
    windowHeight = 600
    windowWidth = 1000

    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()

    x = int((screenWidth/2) - (windowWidth/2))
    y = int((screenHeight/2) - (windowHeight/2))

    searchPage.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, x, y))

    #Barra de Navegação
    barraNav = Menu(searchPage)
    barraNav.add_command(label = "Home", command = lambda:[homePage(),searchPage.destroy()])
    barraNav.add_command(label = "Games", command = lambda:[gamesPage(),searchPage.destroy()])
    barraNav.add_command(label = "User", command = lambda:[userPage(),searchPage.destroy()])
    barraNav.add_command(label = "Notifications", command = lambda:[notificationPage(),searchPage.destroy()])
    barraNav.add_command(label = "Search",command = "")
    barraNav.add_command(label = "Quit", command = searchPage.destroy)

    searchPage.configure(menu = barraNav)

    #Barra de Nome
    frame1 = Frame(searchPage,width=1000,height=50,bg="grey")
    frame1.place(x = 0,y = 0)

    #Nome
    lblName = Label(frame1,text = "GamePick",font = ("Saab",25),bg="grey")
    lblName.place(x = 50 , y = 5)


def loginOrRegister():
    def register():
        check_counter=0
        warn = ""
        data = []
        with open('./data/users.txt',mode='r+', encoding="utf-8")as file:
            for line in file:
                data = line.strip().split(';')  
        if  len(data) > 0 and txtEmail.get() == data[1]:
            warn = "Email already exists!"
        else:
            check_counter += 1
        if txtRepeatPassword.get() == "":
            warn = "Confirm password,cannot be empty!"
        else:
            check_counter += 1

        if txtPassword.get() == "":
            warn = "Password can't be empty!"
        else:
            check_counter += 1

        if txtEmail.get() == "":
            warn = "Email can't be empty!"
        else:
            check_counter += 1

        if txtUsername.get() == "":
            warn = "Name can't be empty!"
        else:
            check_counter += 1

        if txtPassword.get() != txtRepeatPassword.get():
            warn = "Passwords don't match!"
        else:
            check_counter += 1

        if check_counter == 6:        
            try:
                user = [txtUsername.get()+';', txtEmail.get()+';',  txtPassword.get()+';','user']
                file = open('./data/users.txt', "a", encoding="utf-8")
                file.writelines(user)
                file.write("\n")
                file.close()
                messagebox.showinfo('confirmation', 'Register sucessfull!')
                
                
                #What to do next?#
                    
            except Exception as ep:
                
                messagebox.showerror('Error!', ep) 
                

        else:
            
            messagebox.showerror('Error!', warn)
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
    txtPassword = Entry(frameSignIn,show="*",width = 30)
    txtRepeatPassword = Entry(frameSignIn,show="*",width = 30)
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
                        userType = data[3]
                        check_counter += 1
                    else:
                        warn = "Username doesn't exist!"
        except Exception as ep:
            messagebox.showerror('Erro!', ep)
        if upwd == "":
            warn = "Password can't be empty!"
        else:
            check_counter += 1
        if uname == "":
            warn = "Email can't be empty!"
        else:
            check_counter += 1
        if check_counter == 3:
            if (uname == username and upwd == pwd):
                messagebox.showinfo('Login Status', 'Sucessfull Log In!')      
                
                if(userType =="admin"):
                    admin()
                else:    
                    homePage()
            else:
                messagebox.showerror('Login Status', 'Email or password invalid!')
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
    txtPasswordLogin = Entry(frameLogIn,show="*",width = 30)
    txtUsernameLogin.place(x = 150, y = 62)
    txtPasswordLogin.place(x = 150, y = 100)

    btnConfirmLogIn = Button(frameLogIn,text = "Confirm", font = ("Arial Bold",12), width = 8 ,height = 2, command=login)
    btnConfirmLogIn.place(x = 180,y = 150)

def admin():
    window.withdraw()
    ws = Tk()
    ws.title('Admin')

#HOME PAGE
    screen_width = ws.winfo_screenwidth()
    screen_height = ws.winfo_screenheight()

    app_width = 1000
    app_height = 600

    x = (screen_width/2) - (app_width/2)       
    y = (screen_height/2) - (app_height/2)

    ws.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(app_width, app_height, int(x), int(y)))
    #ws.config(bg='light grey')
    ws.config(bg='NavajoWhite2')

    f = ('Times', 14)



    def menu():
        def voltar_atras():
            ws.destroy()
            import HomePage
        # widgets
        menu_frame = Frame(
            ws, 
            bd=2, 
            bg='#CCCCCC',   
            relief=SOLID, 
            padx=10, 
            pady=10
            )
        
        category_btn = Button(
            menu_frame,
            width=12,
            text = "Categories",
            font=f, 
            cursor='hand2',
            command = lambda:[categorias(), menu_frame.place_forget()]) 
        user_btn = Button(
            menu_frame,
            width=12,
            text = "Admins",
            font=f, 
            cursor='hand2',
            command = lambda:[administradores(), menu_frame.place_forget()])
        routes_btn = Button(
            menu_frame,
            width=12,
            text = "Games",
            font=f, 
            cursor='hand2',
            command = lambda:[games(), menu_frame.place_forget()])
        places_btn = Button(
            menu_frame,
            width=12,
            text = "Notifications",
            font=f, 
            cursor='hand2')
        
        voltar_atras_btn = Button(
            menu_frame,
            width=12, 
            text = "Home",
            font=f, 
            
            cursor='hand2',
            command = homePage
        )
        
        button_exit = Button(
            menu_frame,
            width=12,
            text = "Exit",
            font=f, 
            cursor='hand2',
            command = exit)
        
        menu_frame.place(relx=0.5, rely=0.5, anchor=CENTER)


        category_btn.grid(row=0, column=0, pady=10, padx=15)
        user_btn.grid(row=1, column=1, pady=10, padx=20) 
        routes_btn.grid(row=1, column=0, pady=10, padx=20)
        places_btn.grid(row=0, column=1, pady=10, padx=20)
        button_exit.grid(row=2, column=1, pady=10, padx=20)
        voltar_atras_btn.grid(row=2, column=0, pady=10, padx=10)

    def categorias():
        def criar_categoria():
            check_counter=0
            warn = ""
            if category_name.get() == "":
                warn = "Category cannot be empty!"
            else:
                check_counter += 1

            
            data = []
            erro = False
            with open('./data/categories.txt',mode='r+')as file:
                for line in file:
                    data = line.strip().split(';')
                    if  len(data) > 0 and category_name.get() == data[0]:
                        erro = True
            if erro == True:
                warn = "Categoria already exists!"
            else:
                check_counter += 1

            if check_counter == 2:        
                try:
                    user = [category_name.get()]
                    file = open('./data/categories.txt', "a", encoding="utf-8")
                    file.writelines(user)
                    file.write("\n")
                    file.close()
                    messagebox.showinfo('confirmation', 'Category created!')
                    
                    
                except Exception as ep:
                    messagebox.showerror('', ep) 
            else:
                messagebox.showerror('Erro', warn)

        def mostrar_categoria():
            try:  
                tree.delete(*tree.get_children())
                erro = False
                with  open('./data/categories.txt',mode='r+' ,  encoding="utf-8") as file:
                        for line in file:
                            data = line.strip().split(';')
                            tree.insert("", "end", values = (data[0]))
            except Exception as ep:
                messagebox.showwarning('Admin', ep)


        def apagar_categoria():
            curItem = tree.focus()
            tree_data =  tree.item(curItem)["values"]
            cat_line = []
            try:
                cat_line = tree_data[0]
            except Exception as ep:
                messagebox.showerror('Erro', "Select a category!")  
            check_counter=0
            warn = ""
            data = []
            erro = False
            with open('./data/categories.txt',mode='r+' ,  encoding="utf-8") as file:
                chk_file =  []
                for line in file:
                    data = line.strip().split(';')
                    chk_file.append(data[0])
                if tree_data[0] not in chk_file:
                        erro = True    
            if erro == True:
                warn = "Category doesn't exist!"
            else:
                check_counter += 1
            
            if check_counter == 1:   
                # open file in read mode
                with  open('./data/categories.txt',mode='r+' ,  encoding="utf-8") as f:
                    data = f.readlines()
                with  open('./data/categories.txt',mode='w' ,  encoding="utf-8") as f:
                    for line in data :
                        if line.strip("\n") != cat_line: 
                            f.write(line)
                        
                    messagebox.showinfo('confirmation', 'Category deleted!')

            else:
                messagebox.showerror('Erro', warn)


        # Categorias
        main_categoria_frame = Frame (
            ws, 
            bg='NavajoWhite2',
            width=app_width, 
            height=app_height
        )
        category_frame = Frame(
            main_categoria_frame, 
            bd=2, 
            bg='#CCCCCC',
            relief=SOLID, 
            padx=10, 
            pady=10
            )

        tree = ttk.Treeview(
        main_categoria_frame, 
        columns = ("Category"), 
        show = "headings", 
        height=9
        )
        
        tree.column("Category", width = 200,   anchor="c")
        tree.heading("Category", text = "Category")
        tree.place(relx= 0.7, rely=0.5, anchor=CENTER)

        Label(
            category_frame, 
            text="Name", 
            bg='#CCCCCC',
            font=f
            ).grid(row=0, column=0, sticky=W, pady=10)


        category_name = Entry(
            category_frame, 
            font=f
            )

        
        create_category = Button(
            category_frame, 
            width=15, 
            text='Create', 
            font=f, 
            
            cursor='hand2',
            command=criar_categoria
        )
        delete_btn = Button(
            category_frame, 
            width=15, 
            text='Delete', 
            font=f, 
            
            cursor='hand2',
            command=apagar_categoria
        )
        showBtn = Button(
            category_frame, 
            width=15, 
            text='Refresh', 
            font=f, 
        
            cursor='hand2',
            command=mostrar_categoria
        )

        back_btn = Button(
            category_frame, 
            width=15, 
            text='Back', 
            font=f, 
            
            cursor='hand2',
            command=lambda:[menu(), main_categoria_frame.place_forget()]
        )

    
        category_name.grid(row=0, column=1, pady=10, padx=20)
        create_category.grid(row=1, column=1, pady=10, padx=20)
        showBtn.grid(row=1, column=0, pady=10, padx=20)
        delete_btn.grid(row=2, column=1, pady=10, padx=20)
        
        back_btn.grid(row = 2, column = 0, padx = 10, pady = 20)
        category_frame.place(relx=0.3, rely=0.5, anchor= CENTER)
        main_categoria_frame.place(relx=0, rely=0)

    def administradores():
        def createAdmin():
            check_counter=0
            warn = ""
            if pwd_again.get() == "":
                warn = "Confirm Password cannot be empty!"
            else:
                check_counter += 1

            if register_pwd.get() == "":
                warn = "Password cannot be empty"
            else:
                check_counter += 1

            if register_email.get() == "":
                warn = "Email cannot be empty!"
            else:
                check_counter += 1

            if register_name.get() == "":
                warn = "Name cannot be empty!"
            else:
                check_counter += 1

            if register_pwd.get() != pwd_again.get():
                warn = "Passwords don't match!"
            else:
                check_counter += 1
            
            data = []
            erro = False
            with open('./data/users.txt',mode='r+')as file:
                for line in file:
                    data = line.strip().split(';')  
                    if  len(data) > 0 and register_name.get() == data[0]:
                        erro = True
            if erro == True:
                warn = "Name already exists!"

                
            else:
                check_counter += 1

            if check_counter == 6:        
                try:
                    user = [register_name.get()+';', register_email.get()+';',  register_pwd.get()+';','admin']
                    file = open('./data/users.txt', "a", encoding="utf-8")
                    file.writelines(user)
                    file.write("\n")
                    file.close()
                    messagebox.showinfo('confirmation', 'Register Suceeded!')
                    #What to do next?#
                    
                except Exception as ep:
                    messagebox.showerror('Erro!', ep) 
            else:
                messagebox.showerror('Erro!', warn)

        def showAdmin():
            try:  
                tree.delete(*tree.get_children())
                erro = False
                with  open('./data/users.txt',mode='r+' ,  encoding="utf-8") as file:
                        for line in file:
                            data = line.strip().split(';')
                            if data[3] == "admin":
                                tree.insert("", "end", values = (data[0], data[1], data[2]))
            except Exception as ep:
                messagebox.showwarning('Admin', ep)

        def deleteAdmin():
            curItem = tree.focus()
            tree_data =  tree.item(curItem)["values"]
            user_line = []
            try:
                user_line = tree_data[0]+ ";"+ tree_data[1]+ ";"+ tree_data[2]+ ";"+ tree_data[3]
            except Exception as ep:
                messagebox.showerror('Erro', "Select User!")  
            
            check_counter=0
            warn = ""
            data = []
            chk_file =  []
            erro = False
            with open('./data/users.txt',mode='r+' ,  encoding="utf-8") as file:
                for line in file:
                    data = line.strip().split(';')
                    chk_file.append(data[1])
                if tree_data[1] not in chk_file:
                        erro = True    
            if erro == True:
                warn = "User doesn't exist!"
            else:
                check_counter += 1
            
            if len(chk_file) <= 1:
                warn = "You cannot delete the last admin!"
            else:
                check_counter += 1


            if check_counter == 2:   
                # open file in read mode
                with  open('./data/users.txt',mode='r+' ,  encoding="utf-8") as f:
                    data = f.readlines()
                with  open('./data/users.txt',mode='w' ,  encoding="utf-8") as f:
                    for line in data :
                        if line.strip("\n") != user_line: 
                            f.write(line)
                        
                    messagebox.showinfo('confirmation', 'User deleted!')

            else:
                messagebox.showerror('Erro', warn)

        main_users_frame = Frame (
            ws, 
            bg='NavajoWhite2',
            width=app_width, 
            height=app_height
        )

        users_frame = Frame(
            main_users_frame, 
            bd=2, 
            bg='#CCCCCC',
            relief=SOLID, 
            padx=10, 
            pady=20
        )

        tree = ttk.Treeview(
        main_users_frame, 
        columns = ("Name", "Email", "Password"), 
        show = "headings", 
        height=16
        )
        
        tree.column("Nome", width = 130,   anchor="c")
        tree.column("Email", width = 160,  anchor="c") # c- center, e -direita, w- esquerda
        tree.column("Password", width = 130,  anchor="c") 
        tree.heading("Nome", text = "Nome")
        tree.heading("Email", text = "Email")
        tree.heading("Password", text = "Password")
        tree.place(relx= 0.55, rely=0.15)

        Label(
            users_frame, 
            text="Name", 
            bg='#CCCCCC',
            font=f
            ).grid(row=0, column=0, sticky=W, pady=10)

        Label(
            users_frame, 
            text="Email", 
            bg='#CCCCCC',
            font=f
            ).grid(row=1, column=0, sticky=W, pady=10)

        Label(
            users_frame, 
            text="Password", 
            bg='#CCCCCC',
            font=f
            ).grid(row=5, column=0, sticky=W, pady=10)

        Label(
            users_frame, 
            text="Confirm password", 
            bg='#CCCCCC',
            font=f
            ).grid(row=6, column=0, sticky=W, pady=10)

        register_name = Entry(
            users_frame, 
            font=f
            )

        register_email = Entry(
            users_frame, 
            font=f
            )


        register_pwd = Entry(
            users_frame, 
            font=f,
            show='*'
        )
        pwd_again = Entry(
            users_frame, 
            font=f,
            show='*'
        )
        showBtn = Button(
            users_frame, 
            width=15, 
            text='Refresh/Show', 
            font=f, 
        
            cursor='hand2',
            command=showAdmin
        )
        delete_btn = Button(
            users_frame, 
            width=15, 
            text='Delete', 
            font=f, 
        
            cursor='hand2',
            command=deleteAdmin
        )
    
        register_btn = Button(
            users_frame, 
            width=15, 
            text='Add', 
            font=f, 
        
            cursor='hand2',
            command=createAdmin
        )
        back_btn = Button(
            users_frame, 
            width=15, 
            text='Back', 
            font=f, 
        
            cursor='hand2',
            command=lambda:[menu(), main_users_frame.place_forget()]
        )
        register_name.grid(row=0, column=1, pady=10, padx=20)
        register_email.grid(row=1, column=1, pady=10, padx=20) 
        register_pwd.grid(row=5, column=1, pady=10, padx=20)
        pwd_again.grid(row=6, column=1, pady=10, padx=20)
        register_btn.grid(row=7, column=1, pady=10, padx=20)
        showBtn.grid(row=7, column=0, pady=10, padx=20)
        delete_btn.grid(row=8, column=1, pady=10, padx=20)
        back_btn.grid(row=8, column=0, pady=10, padx=20)
        users_frame.place(relx=0.03, rely=0.15)
        main_users_frame.place(relx=0, rely=0)

    def games():
        def browseFiles():
            filename = filedialog.askopenfilename(  initialdir = "./imagens",
                                                title = "Select a File",
                                                filetypes=[
                                                        ("JPEG", "*.jpg"),
                                                        ("PNG", "*.png"),
                                                        ("All files","*.*"), 
                                                        ])
            imagem.insert(0,filename)

        def createGame():
            print(value_inside)
            check_counter=0
            warn = ""
            if value_inside.get() == "":
                warn = "Category cannot be empty!"
            else:
                check_counter += 1

            if imagem.get() == "":
                warn = "Image cannot be empty"
            else:
                check_counter += 1

            if descricao.get() == "":
                warn = "Description cannot be empty!"
            else:
                check_counter += 1
            if titulo.get() == "":
                warn = "Title cannot be empty!"
            else:
                check_counter += 1

            
            data = []
            erro = False
            with open('./data/games.txt',mode='r+')as file:
                for line in file:
                    data = line.strip().split(';')
                    if  len(data) > 0 and titulo.get() == data[0]:
                        erro = True
            if erro == True:
                warn = "Title already exists!"
            else:
                check_counter += 1

            if check_counter == 5:        
                try:
                    game = [titulo.get()+';', descricao.get()+';',  imagem.get()+';',value_inside.get()]
                    file = open('./data/games.txt', "a", encoding="utf-8")
                    file.writelines(game)
                    file.write("\n")
                    file.close()
                    messagebox.showinfo('confirmation', 'Game Added!')
                    
                    
                except Exception as ep:
                    messagebox.showerror('Here', ep) 
            else:
                messagebox.showerror('Erro', warn)
        
        def show_game():
            try:  
                tree.delete(*tree.get_children())
                erro = False
                with  open('./data/games.txt',mode='r+' ,  encoding="utf-8") as file:
                        for line in file:
                            data = line.strip().split(';')
                            tree.insert("", "end", values = (data[0], data[1], data[2], data[3]))
            except Exception as ep:
                messagebox.showwarning('Admin', ep)

        def delete_game():
            curItem = tree.focus()
            tree_data =  tree.item(curItem)["values"]
            rot_line = []
            try:
                rot_line = tree_data[0]+ ";"+ tree_data[1]+ ";"+ tree_data[2]+ ";"+ tree_data[3]
            except Exception as ep:
                messagebox.showerror('Erro', "Select a Game")  
            check_counter=0
            warn = ""
            data = []
            erro = False
            with open('./data/games.txt',mode='r+' ,  encoding="utf-8") as file:
                chk_file =  []
                for line in file:
                    data = line.strip().split(';')
                    chk_file.append(data[0])
                if tree_data[0] not in chk_file:
                        erro = True    
            if erro == True:
                warn = "Game doesn't exist!"
            else:
                check_counter += 1
            
            if check_counter == 1:   
                # open file in read mode
                with  open('./data/games.txt',mode='r+' ,  encoding="utf-8") as f:
                    data = f.readlines()
                with  open('./data/games.txt',mode='w' ,  encoding="utf-8") as f:
                    for line in data :
                        if line.strip("\n") != rot_line: 
                            f.write(line)
                        
                    messagebox.showinfo('confirmation', 'Game delec!')

            else:
                messagebox.showerror('Erro', warn)

        def att_game():
            curItem = tree.focus()
            tree_data =  tree.item(curItem)["values"]
            rot_line = [] 
            check_counter=0
            warn = ""
            if value_inside.get() == "":
                warn = "Category cannot be empty!"
            else:
                check_counter += 1

            if imagem.get() == "":
                warn = "Image cannot be empty!"
            else:
                check_counter += 1

            if descricao.get() == "":
                warn = "Description cannot be empty!"
            else:
                check_counter += 1
            if titulo.get() == "":
                warn = "Title cannot be empty!"
            else:
                check_counter += 1
            try:
                rot_line = tree_data[0]+ ";"+ tree_data[1]+ ";"+ tree_data[2]+ ";"+ tree_data[3]
            except Exception as ep:
                warn = "Select a Game!" 
            else:
                check_counter  +=1
            if check_counter == 5:        
                try:
                    # open file in read mode
                    roteiro = titulo.get()+';'+descricao.get()+';'+imagem.get()+';'+value_inside.get()
                    data = '' 
                    with  open('./data/games.txt',mode='r+' ,  encoding="utf-8") as f:
                        data = f.read()
                        data = data.replace(rot_line, roteiro)
                        f.close()
                    with  open('./data/games.txt',mode='w' ,  encoding="utf-8") as f:
                        f.write(data)
                    
                    messagebox.showinfo('confirmation', 'Game changed!')
                    
                    
                except Exception as ep:
                    messagebox.showerror('Game', ep) 
            else:
                messagebox.showerror('Erro', warn)

        # Game
        main_game_frame = Frame (
            ws, 
            bg='NavajoWhite2',
            width=app_width, 
            height=app_height
        )
        game_frame = Frame(
            main_game_frame, 
            bd=2, 
            bg='#CCCCCC',   
            relief=SOLID, 
            padx=5, 
            pady=17
            )

        tree = ttk.Treeview(
            main_game_frame, 
        columns = ("Title", "Description", "Image", "Category"), 
        show = "headings", 
        height=18
        )
        
        tree.column("Title", width = 100,   anchor="c")
        tree.column("Description", width = 100,  anchor="c") # c- center, e -direita, w- esquerda
        tree.column("Image", width = 120,  anchor="c") 
        tree.column("Category", width = 100,  anchor="c") 
        tree.heading("Title", text = "Title")
        tree.heading("Description", text = "Description")
        tree.heading("Image", text = "Image")
        tree.heading("Category", text = "Category")
        tree.place(relx= 0.55, rely=0.1)

        Label(
            game_frame, 
            text="Name", 
            bg='#CCCCCC',
            font=f
            ).grid(row=0, column=0, pady=10)

        Label(
            game_frame, 
            text="Description", 
            bg='#CCCCCC',
            font=f
            ).grid(row=1, column=0, pady=10)

        Label(
            game_frame, 
            text="Image", 
            bg='#CCCCCC',
            font=f
            ).grid(row=5, column=0, pady=10)

        Label(
            game_frame, 
            text="Category", 
            bg='#CCCCCC',
            font=f
            ).grid(row=6, column=0, pady=10)

        titulo = Entry(
            game_frame, 
            font=f
            )

        descricao = Entry(
            game_frame, 
            font=f,
        ) 
        imagem = Entry(
            game_frame,
            font=f,  
        ) 
        imagem_btn = Button(
            game_frame,
            text = "Image",
            command = browseFiles) 

        # Create the list of options
        options_list = []
        
        with  open('./data/categories.txt',mode='r+' ,  encoding="utf-8") as file:
                        for line in file:
                            data = line.strip().split(';')
                            options_list.append(data[0])
        # Variable to keep track of the option
        # selected in OptionMenu
        value_inside = StringVar(game_frame)
        
        # Set the default value of the variable
        value_inside.set("Select category!")
        
        # Create the optionmenu widget and passing 
        # the options_list and value_inside to it.
        cbCategories = Combobox(game_frame, values = options_list,textvariable=value_inside).grid(row=6, column=1, pady=10)
        

        categoria = Entry(
            game_frame, 
            font=f,
        )
        createGameBtn = Button(
                game_frame, 
                width=15, 
                text='Add Game', 
                font=f, 
                
                cursor='hand2',
                command=createGame
            )
        showBtn = Button(
            game_frame, 
            width=15, 
            text='Refresh', 
            font=f, 
            command=show_game,
            cursor='hand2',
            
        )
        delete_btn = Button(
            game_frame, 
            width=15, 
            text='Delete', 
            font=f, 
            command=delete_game,
            cursor='hand2',
            
        )
        att_btn = Button(
            game_frame, 
            width=15, 
            text='Alter', 
            font=f, 
            command=att_game,
            cursor='hand2',
            
        )
        gameExit = Button(
            game_frame,
            width=15, 
            text = "Back",
            font=f, 
            
            cursor='hand2',
            command = lambda:[menu(), main_game_frame.place_forget()])
        
    
        titulo.grid(row=0, column=1, pady=10, padx=20)
        descricao.grid(row=1, column=1, pady=10, padx=20) 
        imagem.grid(row=5, column=1, pady=10, padx=20)
        imagem_btn.grid(row=5, column=2, columnspan = 2, rowspan = 1, padx = 5, pady = 5)
        """ question_menu.grid(row=6, column=1, pady=10, padx=20) """
        createGameBtn.grid(row=7, column=1, pady=10, padx=20)   
        showBtn.grid(row=7, column=0, pady=10, padx=20)
        delete_btn.grid(row=8, column=0, pady=10, padx=20)
        att_btn.grid(row=8, column=1, pady=10, padx=20)
        gameExit.grid(row = 9, column = 0,
        columnspan = 2, rowspan = 2, padx = 5, pady = 5)
        
        game_frame.place(relx=0.03, rely=0.1)
        main_game_frame.place(relx=0, rely=0)

    
    # infinite loop
    #admin()
    menu()
        


def homePage():
    
    window.withdraw()
    top = Toplevel()
    top.resizable(0,0)
    top.iconbitmap("./assets/design.png") #Não dá,não sei porquê
    top.configure(bg = "NavajoWhite2") 
    top.title("GamePick")
    barraNav = Menu(top)
    barraNav.add_command(label = "Home", command = "")
    barraNav.add_command(label = "Games", command = userPage)
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
    lblPesquisa = Label(framePesquisa,text = "Search",font = ("Arial",12))
    lblPesquisa.place(x = 600, y = 15)

    txtPesquisa = Entry(top,width=40)
    txtPesquisa.place(x = 700,y= 17)

    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()

    x = int((screenWidth/2) - (windowWidth/2))
    y = int((screenHeight/2) - (windowHeight/2))

    top.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, x, y))

    #Barra de Navegação
    barraNav = Menu(top)
    barraNav.add_command(label = "Home", command = "")
    barraNav.add_command(label = "Games", command = lambda:[gamesPage(),top.destroy()])
    barraNav.add_command(label = "User", command = lambda:[userPage(),top.destroy()])
    barraNav.add_command(label = "Notifications", command = lambda:[notificationPage(),top.destroy()])
    barraNav.add_command(label = "Search",command = lambda:[searchPage(),top.destroy()])
    barraNav.add_command(label = "Quit", command = top.destroy)

    top.configure(menu = barraNav)

    #Barra de Nome
    frame1 = Frame(top,width=1000,height=50,bg="grey")
    frame1.place(x = 0,y = 0)

    #Nome
    lblName = Label(frame1,text = "GamePick",font = ("Saab",25),bg="grey")
    lblName.place(x = 50 , y = 5)


    #Jogo Destaque
    panelJogoDestaque2 = PanedWindow(top,width=600,height=350)
    panelJogoDestaque2.place(x = 50, y = 140)



    #Lista de Jogos
    panelGamesList = PanedWindow(top,width=250,height=350)
    panelGamesList.place(x = 700, y = 140)
    gameslbl = Label(top,text="Games Available" , bg="NavajoWhite2").place(x=700,y=110)
    gamesList = Listbox(panelGamesList, width=350, height = 350)
    with open('./data/games.txt',mode='r+', encoding="utf-8")as file:
                for line in file:
                    data1 = line.strip().split(';')
                    print (data1)
                    gamesList.insert(END, data1[0])                          
    gamesList.place(x=0,y=0)
    selection = gamesList.curselection()
    global gameName
    global gameCat
    global gameDesc
    def viewGame():
        
        with open('./data/games.txt',mode='r+')as file:
            for line in file:
                data = line.strip().split(';')

                if selection == data[0]:
                            gameName = data[0]
                            gameDesc = data[1]
                            gameCat = data[3]
                            
            newTop = Toplevel()
            newTop.resizable(0,0)
            newTop.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, x, y))
            newTop.iconbitmap("./assets/design.png") #Não dá,não sei porquê
            newTop.configure(bg = "NavajoWhite2") 
            newTop.title("GamePick")
            LabelGameName = Label(newTop,text=selection)
            LabelGameName.place(x=100,y=100)
            LabelGameCat = Label(newTop,text=gameCat)
            LabelGameCat.place(x=100,y=200)
            LabelGameDesc = Label(newTop,text=gameDesc)
            LabelGameDesc.place(x=100,y=300)
        
        
        top.destroy()

    btnViewGame = Button(top,text="View", command=viewGame)
    btnViewGame.place(x=800,y=500)


def logout():
    MsgBox = messagebox.askquestion('Exit Application','Deseja mesmo efetuar o logout?',icon = 'warning')    
    if MsgBox == 'yes':
        """ user_btn.config(text="Login/Registo", command=openWindow)
        user_name.config(text="") """
    else:
        messagebox.showinfo('Return','Vai retornar ao ecrã da aplicação!')    
            
loginOrRegister()  
window.mainloop()