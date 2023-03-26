
"""
Proyecto final APOO
"""

class Libros:
    def __init__(self, disp_list=list):
        self.disp_list = disp_list
      


class Estado:
    def __init__(self, data_list):
        self.disp = Libros(data_list)
        self.prestado_dict = {}
    

    def add_book(self,name):
        if name in self.disp.disp_list:
            print(f"Ya se tiene {name}")
        
        elif name in self.prestado_dict.keys():
            print(f"Ya se tiene {name}")
        
        else:
            self.disp.disp_list.append(name)
            print(f"Se agregó {name}")

    def del_book(self,name):
        if name in self.disp.disp_list:
            self.disp.disp_list.remove(name)
            print(f"Se eliminó {name}")
        
        elif name in self.prestado_dict.keys():
            del self.prestado_dict[name]
            print(f"Se eliminó {name}")
        
        else:
            print(f"No se tiene {name}")

            
    def get_book(self, name):
        if name in self.disp.disp_list:
            print(f"{name} está disponible")
            
        elif name in self.prestado_dict.keys():
            print(f"{name} fue prestado por {self.prestado_dict[name][0]} por {self.prestado_dict[name][1]} días")
            
        else:
            print(f"No se tiene {name} ")


     
    def prestar(self, name, nom, day):
        if name in self.prestado_dict.keys():
            print(f"{name} ya fue prestado por {self.prestado_list[name][0]} por {self.prestado_list[name][1]}")
        elif name in self.disp.disp_list:
            self.prestado_dict[name] = [nom,day]
            self.disp.disp_list.remove(name)
            print(f"Se prestó {name}")
        else:
            print(f"No se tiene {name}")
    
    def devolver(self,name):
        if name in self.prestado_dict.keys():
           del self.prestado_dict[name]
           self.disp.disp_list.append(name)
           print(f"Se devolvió {name}")
        else:
            print(f"No se ha prestado {name}")
    
    def perdido(self,name):
        if name in self.disp.disp_list:
            self.disp.disp_list.remove(name)
            print(f"Se reportó como perdido {name}")
        
        elif name in self.prestado_dict.keys():
            del self.prestado_dict[name]
            print(f"Se reportó como perdido {name}")
            
        else:
            print(f"No se tiene {name}")
            

def main():
    libros = ["L1","L2","L3","L4"]
    aver = Estado(libros)
    aver.add_book("L5")
    aver.add_book("L3")
    aver.prestar("L3","Juan",10)
    aver.get_book("L3")
    aver.devolver("L3")
    aver.perdido("L1")
    aver.get_book("L1")
    aver.del_book("L5")
    aver.get_book("L5")
    
main()