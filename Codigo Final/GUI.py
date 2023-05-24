from Sistema_Biblioteca import *
from tkinter import *
from tkinter import messagebox
b = Bibliotecario()
c = Cliente()


    
def biblio():
    global biblio_ventana
    biblio_root = Tk()
    biblio_root.wm_title("Sistema de biblioteca: Bibliotecario")
    biblio_root.geometry("400x300")
    biblio_ventana = Ventana_biblio(master=biblio_root)
    main_ventana.master.destroy()
    biblio_ventana.mainloop()


def searchbib(input):
    messagebox.showinfo("Busqueda",b.search_book(str(input)))

def add(input):
    messagebox.showinfo("Añadir",b.add_book(str(input)))

def delete(input):
    messagebox.showinfo("Borrar",b.del_book(str(input)))

def prest():
    messagebox.showinfo("Prestados",b.prestados())

def clie():
    global clie_ventana
    clie_root = Tk()
    clie_root.wm_title("Sistema de biblioteca: Cliente")
    clie_root.geometry("400x400")
    clie_ventana = Ventana_clie(master=clie_root)
    main_ventana.master.destroy()
    clie_ventana.mainloop()

def searchclie(input):
    messagebox.showinfo("Busqueda",c.search_book(str(input)))

def prestarl(input1, input2, input3):
    messagebox.showinfo("Prestar",c.prestar(input1,input2,input3))

def devol(input):
    messagebox.showinfo("Devolver",c.devolver(input))

def verpre(input):
    messagebox.showinfo("Mis prestados",c.ver_prestados(input))

class Ventana(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.menu1()

    def menu1(self):
        login_lbl = Label(self, text="Seleccione el tipo de usuario")
        login_lbl.grid(column=1, row=0)

        bib_button = Button(self, text="Bibliotecario", command=biblio)
        bib_button.grid(column=0, row=1)

        clie_button = Button(self,text="Cliente", command=clie)
        clie_button.grid(column=2, row=1)

class Ventana_biblio(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.menu2()
    
    
    def menu2(self):
        #search_book
        bib_label = Label(self, text="Buscar libro")
        bib_label.pack()
        search_bar = Entry(self)
        search_bar.pack()
        search_button = Button(self, text="Buscar", command=lambda:searchbib(search_bar.get()))
        search_button.pack(padx=4, pady=6)
        #add_book
        bib_label2 = Label(self, text="Añadir libro")
        bib_label2.pack()
        addbookname = Entry(self)
        addbookname.pack()
        add_button = Button(self, text="Añadir", command=lambda:add(addbookname.get()))
        add_button.pack()
        #del_book
        bib_label3 = Label(self, text="Borrar libro")
        bib_label3.pack()
        erase = Entry(self)
        erase.pack()
        del_button = Button(self, text="Borrar", command=lambda: delete(erase.get()))
        del_button.pack()
        #prestados
        prestados_button = Button(self, text="Ver prestados",command=prest)
        prestados_button.pack(pady=12)


class Ventana_clie(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.menu3()
    
    def menu3(self):
        #search_book
        clie_lbl = Label(self, text="Buscar libro")
        clie_lbl.pack()
        searchbar2 = Entry(self)
        searchbar2.pack()
        search_button2 = Button(self, text="Buscar", command=lambda: searchclie(searchbar2.get()))
        search_button2.pack()
        #prestar
        clie_lbl2 = Label(self, text="Prestar libro")
        clie_lbl2.pack(pady=6)
        book_lbl = Label(self, text="Libro")
        name_lbl = Label(self, text="Nombre")
        day_lbl = Label(self, text="Diás que se prestará")
        book_entry = Entry(self)
        name_entry = Entry(self)
        day_entry = Entry(self)
        book_lbl.pack()
        book_entry.pack()
        name_lbl.pack()
        name_entry.pack()
        day_lbl.pack()
        day_entry.pack()
        prestar_button = Button(self, text="Prestar", command=lambda: prestarl(book_entry.get(),name_entry.get(),day_entry.get()))
        prestar_button.pack()
        #devolver
        clie_lbl3 = Label(self, text="Devolver libro")
        clie_lbl3.pack()
        devolver_entry = Entry(self)
        devolver_entry.pack()
        devolver_button = Button(self, text="Devolver",command=lambda: devol(devolver_entry.get()))
        devolver_button.pack()
        #ver_prestados
        clie_lbl4 = Label(self, text="Ver sus prestados")
        clie_lbl4.pack()
        namepre_lbl = Label(self,text="Nombre:")
        namepre_lbl.pack()
        verpre_entry = Entry(self)
        verpre_entry.pack()
        verpre_button = Button(self, text="Ver prestados", command=lambda: verpre(verpre_entry.get()))
        verpre_button.pack()


main_root = Tk()
main_root.wm_title("Sistema de biblioteca")
main_ventana = Ventana(master=main_root)
main_root.geometry("400x200")

