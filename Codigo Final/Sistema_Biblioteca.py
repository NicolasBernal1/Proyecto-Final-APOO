from dataclasses import dataclass
import json
disponibles = []

def actualizar_pres():
    with open("prestados.txt") as f:
        prestados_str1 = f.read()
        prestados_dic = json.loads(prestados_str1)
        return prestados_dic
prestados = actualizar_pres()

class Proveedor:
    def proveer(self):
        with open("disponibles.txt","r") as libros:
            for libro in libros:
                libro = libro.replace("\n", "")
                disponibles.append(libro)
        return disponibles
p = Proveedor()

class Usuario:
    libros = p.proveer()

class Cliente(Usuario):
    pass

@dataclass
class Bibliotecario(Usuario):
    def search_book(self,book:str):
        if book in self.libros:
            return f"{book} está disponible"
        elif book in prestados.keys():
            return f"El libro fue prestado por {prestados[book][0]}, por {prestados[book][1]} días"
        else:
            return f"No se tiene {book}"
    
    def add_book(self, book:str):
        if book in self.libros:
            return f"Ya se tiene {book}"
        elif book in prestados.keys():
            return f"Ya se tiene {book}"
        elif book == "":
            return "No se puede añadir un libro sin nombre"
        else:
            self.libros.append(book)
            with open ("disponibles.txt","a") as f:
                f.write(f"\n{book}")
            return f"Se añadió {book}"
    
    def del_book(self, book:str):
        if book in self.libros:
            self.libros.remove(book)
            with open("disponibles.txt","w") as f:
                f.write("")
            for i in self.libros:
                with open("disponibles.txt","a") as f:
                    f.write(f"\n{i}")
        elif book in prestados.keys():
            return "No se puede borrar un libro prestado"
        elif book == "":
            return "No se puede borrar un libro sin titulo"
        else:
            return f"No se tiene {book}"
        
    def prestados(self):
        with open("prestados.txt") as f:
            pres = f.read()
            return pres


class Cliente(Usuario):
    def search_book(self,book:str):
        if book in self.libros:
            return f"{book} está disponible"
        elif book in prestados.keys():
            return f"El libro ya fue prestado"
        else:
            return f"No se tiene {book}"
    
    def prestar(self, book, name,day:int):
        if book == "" or name == "" or day == "":
            return "Rellene todos los campos"
        elif book in prestados.keys():
            return f"{book} ya fue prestado"
        elif book in self.libros:
            try:
                day = int(day)
                prestados[book] = [name, day]
                prestados_str = json.dumps(prestados)
                with open("prestados.txt","w") as f:
                    f.write("")
                with open("prestados.txt","w") as f:
                    f.write(prestados_str)
                
                self.libros.remove(book)
                with open("disponibles.txt","w") as f:
                    f.write("")
                for i in self.libros:
                    with open("disponibles.txt","a") as f:
                        f.write(f"\n{i}")
                return f"Usted prestó {book}"
            except:
                return "Ingrese un formato valido"  
        else:
            return f"No se tiene {book}"
    def devolver(self, book):
        if book in prestados.keys():
            self.libros.append(book)
            with open("disponibles.txt","w") as f:
                f.write("")
            for i in self.libros:
                with open("disponibles.txt","a") as f:
                    f.write(f"\n{i}")
            del prestados[book]
            prestados_str = json.dumps(prestados)
            with open("prestados.txt","w") as f:
                f.write("")
            with open("prestados.txt","w") as f:
                f.write(prestados_str)
            return f"Usted devolvió {book}"
        else:
            return f"No se ha prestado {book}"

    def ver_prestados(self,name):
        keylist = []
        for keys, comps in prestados.items():
            if name in comps:
                keylist.append(keys)
        return f"Usted ha prestado {keylist}"
                


















        
    
                
        