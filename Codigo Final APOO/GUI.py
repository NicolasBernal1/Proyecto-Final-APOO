from Biblioteca import *
from tkinter import *

def create_client():
    global c
    c = Cliente()
    root2 = Tk()
    root2.wm_title("Sistema de biblioteca: Clientes")
    app2 = Ventana2_Cliente(master=root2)
    root2.geometry("400x200")
    app.master.destroy()
    app2.mainloop()
    

def searchfor_book():
    c.search_book()

def prestarlibro():
    c.prestar()

def devolverlibro():
    c.devolver()

def verprestados():
    c.ver_prestados()

def create_biblio():
    global b
    b = Bibliotecario()

def verdisponibles():
    b.disponibles()
    


class Ventana(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.login_menu()
    
    def login_menu(self):
        login_lbl = Label(self, text="Elija el tipo de usuario")
        login_lbl.pack(pady=6)

        cliente_bt = Button(self, text="Cliente", command= create_client)
        cliente_bt.pack(pady=10)
    
        biblio_bt = Button(self, text="bibliotecario", command= create_biblio)
        biblio_bt.pack(pady=10)

        exit_button = Button(self, text="Close", command=lambda:self.master.destroy())
        exit_button.pack()

class Ventana2_Cliente(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack
        self.option_menu()
        self.exit()

    def option_menu(self):
        searchbook_button = Button(self, text="Buscar libro", command=searchfor_book)
        searchbook_button.pack()

        prestar_button = Button(self, text="Prestar libro",command=prestarlibro)
        prestar_button.pack()
    
        devolver_button = Button(self, text="Devolver libro", command= devolverlibro)
        devolver_button.pack()

        ver_prestados_button = Button(self, text="Ver prestados", command= verprestados)
        ver_prestados_button.pack()

        disponibles_button = Button(self, text="Ver libros disponibles", command=verdisponibles)
        disponibles_button.pack()

    def exit(self):
        exit_button = Button(self, text="Close", command=lambda: self.master.destroy)
        exit_button.pack()

root = Tk()
root.wm_title("Sistema de libreria")
app = Ventana(master=root)
root.geometry("400x200")
app.mainloop()






