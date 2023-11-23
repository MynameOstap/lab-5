class Room():
    def __init__(self):
        self.appliances = [] 
    def Rearrengement(self,x,y,new_x,new_y):
        for appliance in self.appliances:
            if appliance.get_coordinates() ==  (x,y):
                appliance.set_coordinates(new_x, new_y) 
    
    def add_appliance(self, appliance: 'Appliance'):
        self.appliances.append(appliance)
    def __str__(self) -> str:
        return f'Кімната:{self.appliances}'

    def remove_appliance(self,x, y):
        for appliance in self.appliances:
            if appliance.get_coordinates() ==  (x,y):
                self.appliances.remove(appliance)
                
class Appliance:
    def __init__(self, x:float, y: float):
        self.coordinates = x, y
    
    def set_coordinates(self, x, y):
        self.coordinates = x, y
    def get_coordinates(self):
        return self.coordinates

    
class Bed(Appliance):
    def __init__(self, x:float, y:float, color:str):
        super().__init__(x,y)
        self.color = color
    def set_color(self, color: str):
        self.color = color
    def get_color(self):
        return self.color 
    
    def __repr__(self) -> str:
        return f'Ліжко x = {self.coordinates} Колір = {self.color} '

    

class Table(Appliance):
    def __init__(self,x:float, y:float, material:str):
        super().__init__(x,y)
        self.material = material
    def __repr__(self):
        return f'Стіл xy = {self.coordinates} Матеріл = {self.material} '
         
    
    def set_material(self, material:str):
        self.material = material
    def get_material(self):
        return self.material


    

class Carpet(Appliance):
    def __init__(self, x:float, y:float, picture:str):
        super().__init__(x,y)
        self.picture = picture
    def set_picture(self, picture:str):
        self.picture = picture
    def get_picture(self):
        return self.picture
    def __repr__(self) -> str:
        return f'Килим xy = {self.coordinates} Орнамент = {self.picture} '
def main():
    room = Room()
    room.add_appliance(Bed(1,2,'Маквін'))
    room.add_appliance(Table(4,3,'Тротил'))
    room.add_appliance(Carpet(3,6, 'Біллі Геррінгтон i Джоні Сінс обнімаються'))
    print(room)
    room.remove_appliance(1,2)
    print(room)
    room.Rearrengement(4,3,8,7)
    print(room)
if __name__ == '__main__':
    main()



