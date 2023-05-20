
from dataclasses import dataclass
from abc import ABC, abstractmethod

prestados = {}

@dataclass
class Libros:
    disponibles:list


@dataclass
class Usuario(ABC):
    libros:Libros
    name:str

    @abstractmethod
    def search_book(self, book:str):
        pass

    def disponibles(self):
        for row in self.libros.disponibles:
            print(row)
        
@dataclass
class Bibliotecario(Usuario):
    def search_book(self, book:str):
        if book in self.libros.disponibles:
            print(f"{book} está disponible")
        elif book in prestados.keys():
            print(f"{book} ya fue prestado por {prestados[book][0]}, por {prestados[book][1]} días")
        else:
            print(f"No se tiene {book}")

    def add_book(self, book):
        if book in self.libros.disponibles:
            print(f"{book} ya se tiene")
        elif book in prestados.keys():
            print(f"{book} ya se tiene y fue prestado por {prestados[book][0]}, por {prestados[book][1]} días")
        else:
            self.libros.disponibles.append(book)
            print(f"Se añadió {book}")

    def del_book(self, book):
        if book in self.libros.disponibles:
            while True:
                r = input(f"Seguro que quiere eliminar {book}?(y/n)")
                if r.lower() == "n":
                    print(f"No se eliminará {book}")
                    break
                elif r.lower() == "y":
                    self.libros.disponibles.remove(book)
                    print(f"Se eliminó {book}")
                    break
                else:
                    pass
        elif book in prestados.keys():
            print("No se puede eliminar un libro prestado")
        else:
            print(f"No se tiene {book}")

    def prestados(self):
        print(prestados)

class Cliente(Usuario):
    def search_book(self, book:str):
        if book in self.libros.disponibles:
            print(f"{book} está disponible")
        elif book in prestados.keys():
            print(f"{book} ya fue prestado")
        else:
            print(f"No se tiene {book}")

    def prestar(self, book:str, day:int):
        if book in self.libros.disponibles:
            prestados[book] = [self.name,day]
            self.libros.disponibles.remove(book)
            print(f"Usted prestó {book} por {day} días")
        elif book in prestados.keys():
            print(f"{book} ya fue prestado")
        else:
            print(f"No se tiene {book}")
            

    def devolver(self, book):
        if book in prestados.keys():
            self.libros.disponibles.append(book)
            del prestados[book]
            print(f"Usted devolvio {book}")
        else:
            print(f"No se ha prestado {book}")



D = Libros(["Libro1","Libro2","Libro3","Libro4","Libro5","Libro6"])

B = Bibliotecario(D,"Juan")
C = Cliente(D,"Pepe")


"""
B.disponibles()
C.disponibles()
C.prestar("Libro6",7)
C.prestar("Libro6",7)
C.search_book("Libro6")
B.search_book("Libro6")
B.disponibles()
B.prestados()
"""

