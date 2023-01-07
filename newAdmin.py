import os
import os.path
from pickle import FRAME
from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
from tkinter import filedialog
from tkinter.ttk import Combobox
from traceback import FrameSummary


if not os.path.isfile('./data/users.txt'):
    file = open('users.txt', mode='w+', encoding="utf-8")
    file.writelines(['João',';','admin',';','admin123',';','admin'])
    file.write("\n")
    file.close()

if not os.path.isfile('./data/categories.txt'):
    file = open('categories.txt', mode='w+', encoding="utf-8")
    file.close()    

if not os.path.isfile('./data/games.txt'):
    file = open('games.txt', mode='w+', encoding="utf-8")
    file.close()    




ws = Tk()
ws.title('Admin')


screen_width = ws.winfo_screenwidth()
screen_height = ws.winfo_screenheight()

app_width = 1000
app_height = 600

x = (screen_width/2) - (app_width/2)       
y = (screen_height/2) - (app_height/2)

ws.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(app_width, app_height, int(x), int(y)))
#ws.config(bg='light grey')
ws.config(bg='#fff')

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
        command = lambda:[roteiros(), menu_frame.place_forget()])
    places_btn = Button(
        menu_frame,
        width=12,
        text = "Notifications",
        font=f, 
        cursor='hand2',
        command = lambda:[locais(), menu_frame.place_forget()])
    
    voltar_atras_btn = Button(
        menu_frame,
        width=12, 
        text = "Home",
        font=f, 
        
        cursor='hand2',
        command = voltar_atras
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
        bg='#fff',
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
        text="Nome", 
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
    apagar_btn = Button(
        category_frame, 
        width=15, 
        text='Delete', 
        font=f, 
        
        cursor='hand2',
        command=apagar_categoria
    )
    mostrar_btn = Button(
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
    mostrar_btn.grid(row=1, column=0, pady=10, padx=20)
    apagar_btn.grid(row=2, column=1, pady=10, padx=20)
    
    back_btn.grid(row = 2, column = 0, padx = 10, pady = 20)
    category_frame.place(relx=0.3, rely=0.5, anchor= CENTER)
    main_categoria_frame.place(relx=0, rely=0)

def administradores():
    def criar_administradores():
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
                if  len(data) > 0 and register_email.get() == data[1]:
                    erro = True
        if erro == True:
            warn = "Email already exists!"
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

    def mostrar_administradores():
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

    def apagar_administradores():
        curItem = tree.focus()
        tree_data =  tree.item(curItem)["values"]
        user_line = []
        try:
            user_line = tree_data[0]+ ";"+ tree_data[1]+ ";"+ tree_data[2]+ ";"+ tree_data[3]
        except Exception as ep:
            messagebox.showerror('Erro', "Select User")  
        
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
            warn = "You cannot delete last admin!"
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
        bg='#fff',
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
    columns = ("Nome", "Email", "Password"), 
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
        text="Nome", 
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
        text="Confirmar password", 
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
    mostrar_btn = Button(
        users_frame, 
        width=15, 
        text='Mostar', 
        font=f, 
       
        cursor='hand2',
        command=mostrar_administradores
    )
    apagar_btn = Button(
        users_frame, 
        width=15, 
        text='Apagar', 
        font=f, 
       
        cursor='hand2',
        command=apagar_administradores
    )
   
    register_btn = Button(
        users_frame, 
        width=15, 
        text='Registo', 
        font=f, 
       
        cursor='hand2',
        command=criar_administradores
    )
    back_btn = Button(
        users_frame, 
        width=15, 
        text='Voltar atrás', 
        font=f, 
       
        cursor='hand2',
        command=lambda:[menu(), main_users_frame.place_forget()]
    )
    register_name.grid(row=0, column=1, pady=10, padx=20)
    register_email.grid(row=1, column=1, pady=10, padx=20) 
    register_pwd.grid(row=5, column=1, pady=10, padx=20)
    pwd_again.grid(row=6, column=1, pady=10, padx=20)
    register_btn.grid(row=7, column=1, pady=10, padx=20)
    mostrar_btn.grid(row=7, column=0, pady=10, padx=20)
    apagar_btn.grid(row=8, column=1, pady=10, padx=20)
    back_btn.grid(row=8, column=0, pady=10, padx=20)
    users_frame.place(relx=0.03, rely=0.15)
    main_users_frame.place(relx=0, rely=0)

def roteiros():
    def browseFiles():
        filename = filedialog.askopenfilename(  initialdir = "./imagens",
                                            title = "Select a File",
                                            filetypes=[
                                                    ("JPEG", "*.jpg"),
                                                    ("PNG", "*.png"),
                                                    ("All files","*.*"), 
                                                    ])
        imagem.insert(0,filename)

    def criar_roteiro():
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
                roteiro = [titulo.get()+';', descricao.get()+';',  imagem.get()+';',value_inside.get()]
                file = open('./data/games.txt', "a", encoding="utf-8")
                file.writelines(roteiro)
                file.write("\n")
                file.close()
                messagebox.showinfo('confirmation', 'Game Added!')
                
                
            except Exception as ep:
                messagebox.showerror('Here', ep) 
        else:
            messagebox.showerror('Erro', warn)
    
    def mostrar_roteiro():
        try:  
            tree.delete(*tree.get_children())
            erro = False
            with  open('./data/games.txt',mode='r+' ,  encoding="utf-8") as file:
                    for line in file:
                        data = line.strip().split(';')
                        tree.insert("", "end", values = (data[0], data[1], data[2], data[3]))
        except Exception as ep:
            messagebox.showwarning('Admin', ep)

    def apagar_roteiro():
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

    def atualizar_roteiro():
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
            warn = "Select a Game" 
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
                
                messagebox.showinfo('confirmation', 'Game Changed!')
                
                
            except Exception as ep:
                messagebox.showerror('Roteiro', ep) 
        else:
            messagebox.showerror('Erro', warn)
    # Roteiro
    main_roteiro_frame = Frame (
        ws, 
        bg='#fff',
        width=app_width, 
        height=app_height
    )
    roteiro_frame = Frame(
        main_roteiro_frame, 
        bd=2, 
        bg='#CCCCCC',   
        relief=SOLID, 
        padx=5, 
        pady=17
        )

    tree = ttk.Treeview(
        main_roteiro_frame, 
    columns = ("Titulo", "Descrição", "Imagem", "Categoria"), 
    show = "headings", 
    height=18
    )
    
    tree.column("Titulo", width = 100,   anchor="c")
    tree.column("Descrição", width = 100,  anchor="c") # c- center, e -direita, w- esquerda
    tree.column("Imagem", width = 120,  anchor="c") 
    tree.column("Categoria", width = 100,  anchor="c") 
    tree.heading("Titulo", text = "Título")
    tree.heading("Descrição", text = "Descrição")
    tree.heading("Imagem", text = "Imagem")
    tree.heading("Categoria", text = "Categoria")
    tree.place(relx= 0.55, rely=0.1)

    Label(
        roteiro_frame, 
        text="Título", 
        bg='#CCCCCC',
        font=f
        ).grid(row=0, column=0, pady=10)

    Label(
        roteiro_frame, 
        text="Descrição", 
        bg='#CCCCCC',
        font=f
        ).grid(row=1, column=0, pady=10)

    Label(
        roteiro_frame, 
        text="Imagem", 
        bg='#CCCCCC',
        font=f
        ).grid(row=5, column=0, pady=10)

    Label(
        roteiro_frame, 
        text="Categoria", 
        bg='#CCCCCC',
        font=f
        ).grid(row=6, column=0, pady=10)

    titulo = Entry(
        roteiro_frame, 
        font=f
        )

    descricao = Entry(
        roteiro_frame, 
        font=f,
    ) 
    imagem = Entry(
        roteiro_frame,
        font=f,  
    ) 
    imagem_btn = Button(
        roteiro_frame,
        text = "Imagem",
        command = browseFiles) 
    # Create the list of options
    options_list = []
    
    with  open('./data/categories.txt',mode='r+' ,  encoding="utf-8") as file:
                    for line in file:
                        data = line.strip().split(';')
                        options_list.append(data[0])
    # Variable to keep track of the option
    # selected in OptionMenu
    value_inside = StringVar(roteiro_frame)
    
    # Set the default value of the variable
    value_inside.set("Select category")
    
    # Create the optionmenu widget and passing 
    # the options_list and value_inside to it.
    cbCategories = Combobox(roteiro_frame, values = options_list,textvariable=value_inside).grid(row=6, column=1, pady=10)
    

    categoria = Entry(
        roteiro_frame, 
        font=f,
    )
    criar_roteiro_btn = Button(
            roteiro_frame, 
            width=15, 
            text='Add Game', 
            font=f, 
            
            cursor='hand2',
            command=criar_roteiro
        )
    mostrar_btn = Button(
        roteiro_frame, 
        width=15, 
        text='Mostrar', 
        font=f, 
        command=mostrar_roteiro,
        cursor='hand2',
        
    )
    apagar_btn = Button(
        roteiro_frame, 
        width=15, 
        text='Delete', 
        font=f, 
        command=apagar_roteiro,
        cursor='hand2',
        
    )
    atualizar_btn = Button(
        roteiro_frame, 
        width=15, 
        text='Atualizar', 
        font=f, 
        command=atualizar_roteiro,
        cursor='hand2',
        
    )
    roteiro_exit = Button(
        roteiro_frame,
        width=15, 
        text = "Back",
        font=f, 
        
        cursor='hand2',
        command = lambda:[menu(), main_roteiro_frame.place_forget()])
    
   
    titulo.grid(row=0, column=1, pady=10, padx=20)
    descricao.grid(row=1, column=1, pady=10, padx=20) 
    imagem.grid(row=5, column=1, pady=10, padx=20)
    imagem_btn.grid(row=5, column=2, columnspan = 2, rowspan = 1, padx = 5, pady = 5)
    """ question_menu.grid(row=6, column=1, pady=10, padx=20) """
    criar_roteiro_btn.grid(row=7, column=1, pady=10, padx=20)   
    mostrar_btn.grid(row=7, column=0, pady=10, padx=20)
    apagar_btn.grid(row=8, column=0, pady=10, padx=20)
    atualizar_btn.grid(row=8, column=1, pady=10, padx=20)
    roteiro_exit.grid(row = 9, column = 0,
       columnspan = 2, rowspan = 2, padx = 5, pady = 5)
       
    roteiro_frame.place(relx=0.03, rely=0.1)
    main_roteiro_frame.place(relx=0, rely=0)

def locais():

    def browseFiles():
        filename = filedialog.askopenfilename(  initialdir = "./imagens",
                                            title = "Select a File",
                                            filetypes=[
                                                    ("JPEG", "*.jpg"),
                                                    ("PNG", "*.png"),
                                                    ("All files","*.*"), 
                                                    ])
        imagem_local.insert(0,filename)

    def criar_local():
        
        check_counter=0
        warn = ""
        if imagem_local.get() == "":
                warn = "Image cannot be empty!"
        else:
            check_counter += 1

        if descricao.get() == "":
            warn = "Description cannot be empty!"
        else:
            check_counter += 1
        if local_name.get() == "":
            warn = "Local não pode estar vazio!"
        else:
            check_counter += 1
        data = []
        erro = False
        with open('locais.txt',mode='r+', encoding="utf-8")as file:
            for line in file:
                data = line.strip().split(';')
                print(data)
                if  len(data) > 0 and local_name.get() == data[0]:
                    erro = True
        if erro == True:
            warn = "Local já existe!"
        else:
            check_counter += 1

        if check_counter == 4:        
            try:
                local = [local_name.get()+';', descricao.get()+';',  imagem_local.get()]
                file = open('locais.txt', "a", encoding="utf-8")
                file.writelines(local)
                file.write("\n")
                file.close()
                messagebox.showinfo('confirmation', 'Local criado com sucesso!')
                
                
            except Exception as ep:
                messagebox.showerror('', ep) 
        else:
            messagebox.showerror('Erro', warn)

    def mostrar_local():
        try:  
            tree.delete(*tree.get_children())
            erro = False
            with  open('locais.txt',mode='r+' ,  encoding="utf-8") as file:
                    for line in file:
                        data = line.strip().split(';')
                        tree.insert("", "end", values = (data[0], data[1], data[2]))
        except Exception as ep:
            messagebox.showwarning('Admin', ep)


    def apagar_local():
        curItem = tree.focus()
        tree_data =  tree.item(curItem)["values"]
        loc_line = []
        try:
            loc_line = tree_data[0]+ ";"+ tree_data[1]+ ";"+ tree_data[2]
        except Exception as ep:
            messagebox.showerror('Erro', "Precisa de selecionar um local")  
        check_counter=0
        warn = ""
        data = []
        erro = False
        with open('locais.txt',mode='r+' ,  encoding="utf-8") as file:
            chk_file =  []
            for line in file:
                data = line.strip().split(';')
                chk_file.append(data[0])
            if tree_data[0] not in chk_file:
                    erro = True    
        if erro == True:
            warn = "Local não existe!"
        else:
            check_counter += 1
        
        if check_counter == 1:   
            # open file in read mode
            with  open('locais.txt',mode='r+' ,  encoding="utf-8") as f:
                data = f.readlines()
            with  open('locais.txt',mode='w' ,  encoding="utf-8") as f:
                for line in data :
                    if line.strip("\n") != loc_line: 
                        f.write(line)
                    
                messagebox.showinfo('confirmation', 'Local apagado com sucesso!')

        else:
            messagebox.showerror('Erro', warn)

    main_local_frame = Frame (
        ws, 
        bg='#fff',
        relief=SOLID, 
        width=app_width, 
        height=app_height
    )

    local_frame = Frame(
        main_local_frame, 
        bd=2, 
        bg='#CCCCCC',
        relief=SOLID, 
        padx=10, 
        pady=10
        )


    tree = ttk.Treeview(
    main_local_frame, 
    columns = ("Local", "Descricao", "Imagem"), 
    show = "headings", 
    height=9
    )
    
    tree.column("Local", width = 140,   anchor="c")
    tree.column("Descricao", width = 140,   anchor="c")
    tree.column("Imagem", width = 150,   anchor="c")
    tree.heading("Local", text = "Local")
    tree.heading("Descricao", text = "Descrição")
    tree.heading("Imagem", text = "Imagem")
    tree.place(relx= 0.55, rely=0.2)


    Label(
        local_frame, 
        text="Local", 
        bg='#CCCCCC',
        font=f
        ).grid(row=0, column=0, pady=10)

    Label(
        local_frame, 
        text="Descrição", 
        bg='#CCCCCC',
        font=f
        ).grid(row=1, column=0, pady=10)

    Label(
        local_frame, 
        text="Imagem", 
        bg='#CCCCCC',
        font=f
        ).grid(row=5, column=0, pady=10)

    local_name = Entry(
        local_frame, 
        font=f
        )
    descricao = Entry(
        local_frame, 
        font=f,
    ) 
    imagem_local = Entry(
        local_frame,
        font=f,  
    ) 
    imagem_local_btn = Button(
        local_frame,
        text = "Imagem",
        command = browseFiles) 
    

    criar_local_btn = Button(
        local_frame, 
        width=15, 
        text='Criar', 
        font=f,
        cursor='hand2',
        command=criar_local
    )

    apagar_btn = Button(
        local_frame, 
        width=15, 
        text='Apagar', 
        font=f, 
        cursor='hand2',
        command=apagar_local
    )
    mostrar_btn = Button(
        local_frame, 
        width=15, 
        text='Mostrar', 
        font=f, 
        cursor='hand2',
        command=mostrar_local
    )
    button_exit = Button(
        local_frame,
        width=15, 
        text = "Voltar atrás",
        font=f, 
        
        cursor='hand2',
        command = lambda:[menu(), main_local_frame.place_forget()])

    local_name.grid(row=0, column=1, pady=10, padx=20)
    descricao.grid(row=1, column=1, pady=10, padx=20)
    imagem_local.grid(row=5, column=1, pady=10, padx=20)
    imagem_local_btn.grid(row=5, column=2, columnspan = 2, rowspan = 1, padx = 5, pady = 5) 
    mostrar_btn.grid(row=7, column=0, pady=10, padx=20)
    criar_local_btn.grid(row=7, column=1, pady=10, padx=20)
    button_exit.grid(row=8, column=0, pady=10, padx=20)
    apagar_btn.grid(row=8, column=1, pady=10, padx=20)
    

    local_frame.place(relx=0.02, rely=0.2)
    main_local_frame.place(relx=0, rely=0)
 

# infinite loop
#admin()
menu()
ws.mainloop()    