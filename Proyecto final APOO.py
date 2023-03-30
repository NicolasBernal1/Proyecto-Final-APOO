
"""
Proyecto final APOO
"""
prestado_dict = {}
class Libros:
    def __init__(self, disp_list=list):
        self.disp_list = disp_list
      


class Bibliotecario:
    def __init__(self, data_list:list,name:str):
        self.disp = Libros(data_list)
        self.name = name
        
    
    def get_book(self, name:str):
        if name in self.disp.disp_list:
            print(f"{name} está disponible")
            
        elif name in prestado_dict.keys():
            print(f"{name} fue prestado por {prestado_dict[name][0]} por {prestado_dict[name][1]} días")
            
        else:
            print(f"No se tiene {name} ")
     
    def add_book(self,name:str):
        if name in self.disp.disp_list:
            print(f"Ya se tiene {name}")
        
        elif name in prestado_dict.keys():
            print(f"Ya se tiene {name}")
        
        else:
            self.disp.disp_list.append(name)
            print(f"Se agregó {name}")
        
    def del_book(self,name:str):
        if name in self.disp.disp_list:
            self.disp.disp_list.remove(name)
            print(f"Se eliminó {name}")
        
        elif name in prestado_dict.keys():
            del prestado_dict[name]
            print(f"Se eliminó {name}")
        
        else:
            print(f"No se tiene {name}")
        
    def perdido(self,name:str):
        if name in self.disp.disp_list:
            self.disp.disp_list.remove(name)
            print(f"Se reportó como perdido {name}")
        
        elif name in prestado_dict.keys():
            del prestado_dict[name]
            print(f"Se reportó como perdido {name}")
            
        else:
            print(f"No se tiene {name}")
    
    def show_disp(self):
        print(self.disp.disp_list)
    
    def show_prestado(self):
        print(prestado_dict)



class Cliente:
    def __init__(self,data_list:list, name:str):
        self.disp = Libros(data_list)
        self.name = name
        

    def get_book(self, name:str):
        if name in self.disp.disp_list:
            print(f"{name} está disponible")
            
        elif name in prestado_dict.keys():
            print(f"{name} fue prestado por {prestado_dict[name][0]} por {prestado_dict[name][1]} días")
            
        else:
            print(f"No se tiene {name} ")

    def prestar(self, name:str, day:int):
        if name in prestado_dict.keys():
            print(f"{name} ya fue prestado por {prestado_dict[name][0]} por {prestado_dict[name][1]} días")
        elif name in self.disp.disp_list:
            prestado_dict[name] = [self.name,day]
            self.disp.disp_list.remove(name)
            print(f"{self.name} prestó {name} por {day} días")
        else:
            print(f"No se tiene {name}")
    
    def devolver(self,name:str):
        if name in prestado_dict.keys():
           del prestado_dict[name]
           self.disp.disp_list.append(name)
           print(f"Se devolvió {name}")
        else:
            print(f"No se ha prestado {name}")

    def show_disp(self):
        print(self.disp.disp_list)



def main():
    lista = ["L1","L2","L3","L4"]
    b1 = Bibliotecario(lista,"Juan")
    b1.get_book("L1")
    b1.add_book("L5")
    b1.del_book("L2")
    b1.perdido("L4")
    b1.show_disp()
    b1.show_prestado()
    print("//////////////////////////////")
    c1 = Cliente(lista,"Pedro")
    c1.get_book("L1")
    c1.prestar("L3",3)
    c1.get_book("L3")
    c1.prestar("L3",2)
    c1.devolver("L3")
    c1.show_disp()
    
    
main()