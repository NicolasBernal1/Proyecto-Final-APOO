
from dataclasses import dataclass
from tkinter import *

prestados = {}
libros = ["Libro1","Libro2","Libro3","Libro4","Libro5","Libro6"]



@dataclass
class Usuario:
    name=""

   
    def search_book(self): 
        pass

    def disponibles(self): 
        print(libros) 
        
@dataclass
class Bibliotecario(Usuario):
    def search_book(self):
        book_entry = Entry(self)
        book_entry.pack()
        book = book_entry.get()
        if book in libros:
            print(f"{book} está disponible")
        elif book in prestados.keys():
            print(f"{book} ya fue prestado por {prestados[book][0]}, por {prestados[book][1]} días")
        else:
            print(f"No se tiene {book}")

    def add_book(self):
        book_entry = Entry(self)
        book_entry.pack()
        book = book_entry.get()
        if book in libros:
            print(f"{book} ya se tiene")
        elif book in prestados.keys():
            print(f"{book} ya se tiene y fue prestado por {prestados[book][0]}, por {prestados[book][1]} días")
        else:
            libros.append(book)
            print(f"Se añadió {book}")

    def del_book(self):
        book_entry = Entry(self)
        book_entry.pack()
        book = book_entry.get()
        if book in libros:
            while True:
                r = input(f"Seguro que quiere eliminar {book}?(y/n)")
                if r.lower() == "n":
                    print(f"No se eliminará {book}")
                    break
                elif r.lower() == "y":
                    libros.remove(book)
                    print(f"Se eliminó {book}")
                    break
                else:
                    pass
        elif book in prestados.keys():
            print("No se puede eliminar un libro prestado")
        else:
            print(f"No se tiene {book}")

    def prestados(self):
        prestados_label = Label(self, textvariable=str(prestados))
        prestados_label.pack()
    

class Cliente(Usuario):
    def search_book(self):
        book_entry = Entry(self)
        book_entry.pack()
        book = book_entry.get()
        if book in libros:
            print(f"{book} está disponible")
        elif book in prestados.keys():
            print(f"{book} ya fue prestado")
        else:
            print(f"No se tiene {book}")

    def prestar(self):
        name_entry = Entry(self)
        name_entry.pack()
        self.name = name_entry.get()
        book_entry = Entry(self)
        book_entry.pack()
        book = book_entry.get()
        try:
            day = int(input("Cuantos días se prestará: "))
            if book in libros:
                prestados[book] = [self.name,day]
                libros.remove(book)
                print(f"Usted prestó {book} por {day} días")
            elif book in prestados.keys():
                print(f"{book} ya fue prestado")
            else:
                print(f"No se tiene {book}")
        except:
            print("Ingrese un formato valido")
            self.prestar()
            

    def devolver(self):
        book_entry = Entry(self)
        book_entry.pack()
        book = book_entry.get()
        if book in prestados.keys():
            libros.append(book)
            del prestados[book]
            print(f"Usted devolvio {book}")
        else:
            print(f"No se ha prestado {book}")

    def ver_prestados(self):
        for key,comps in prestados.items():
            if self.name in comps:
                prestados_label = Label(self, text=f"Usted tiene prestado {key}, por {comps[1]} días")
                prestados_label.pack()



