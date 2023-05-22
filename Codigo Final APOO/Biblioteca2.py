from dataclasses import dataclass


prestados = {}
db = ["Libro1","Libro2","Libro3","Libro4","Libro5","Libro6"]
blacklist = []

@dataclass
class Proveedor:
      libros:list

      def deliver(self):
          return list(self.libros)
p = Proveedor(db)

@dataclass
class Usuario:
    name = ""
    libros = p.deliver()

    def search_book(self): 
        pass

    def disponibles(self): 
        print(self.libros) 
        
@dataclass
class Bibliotecario(Usuario):
    def search_book(self):
        book = input("Ingresar libro: ")
        if book in self.libros:
            print(f"{book} está disponible")
        elif book in prestados.keys():
            print(f"{book} ya fue prestado por {prestados[book][0]}, por {prestados[book][1]} días")
        else:
            print(f"No se tiene {book}")

    def add_book(self):
        book = input("Ingresar libro a agregar: ")
        if book in self.libros:
            print(f"{book} ya se tiene")
        elif book in prestados.keys():
            print(f"{book} ya se tiene y fue prestado por {prestados[book][0]}, por {prestados[book][1]} días")
        else:
            self.libros.append(book)
            print(f"Se añadió {book}")

    def del_book(self):
        book = input("Ingresar libro a borrar: ")
        if book in self.libros:
            while True:
                r = input(f"Seguro que quiere eliminar {book}?(y/n)")
                if r.lower() == "n":
                    print(f"No se eliminará {book}")
                    break
                elif r.lower() == "y":
                    self.libros.remove(book)
                    print(f"Se eliminó {book}")
                    break
                else:
                    pass
        elif book in prestados.keys():
            print("No se puede eliminar un libro prestado")
        else:
            print(f"No se tiene {book}")

    def reportar(self, nombre):
        for keys,comps in prestados.items():
            if nombre in comps:
                blacklist.append(nombre)
                del prestados[keys]
                print(f"Se añadió a {nombre} a la lista negra")
                break
        


    def prestados(self):
        print(prestados)
    
    

class Cliente(Usuario):
    def search_book(self):
        book = input("Ingresar libro: ")
        if book in self.libros:
            print(f"{book} está disponible")
        elif book in prestados.keys():
            print(f"{book} ya fue prestado")
        else:
            print(f"No se tiene {book}")

    def prestar(self):
        self.name = input("Imgrese su nombre: ")
        book = input("Ingresar libro a prestar: ")
        if self.name in blacklist:
            print("No puede prestar un libro estando en la lista negra")
        else: 
            try:
                day = int(input("Cuantos días se prestará: "))
                if book in self.libros:
                    prestados[book] = [self.name,day]
                    self.libros.remove(book)
                    print(f"Usted prestó {book} por {day} días")
                elif book in prestados.keys():
                    print(f"{book} ya fue prestado")
                else:
                    print(f"No se tiene {book}")
            except:
                print("Ingrese un formato valido")
                self.prestar()
            

    def devolver(self):
        book = input("Ingresar libro a devolver: ")
        if book in prestados.keys():
            self.libros.append(book)
            del prestados[book]
            print(f"Usted devolvio {book}")
        else:
            print(f"No se ha prestado {book}")

    def ver_prestados(self):
        for key,comps in prestados.items():
            if self.name in comps:
                print(f"Usted tiene prestado {key}, por {comps[1]} días")
                