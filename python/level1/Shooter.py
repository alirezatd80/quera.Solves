class Shooter:
    
    Guns = ['Submachine Gun','Assault Rifle','Pistol','Shotgun','Sniper Rifle']
    Board  = [100,200,80,50,1000]
    Power = [10,20,8,40,30]
    
    SizeTir = [0.5,1,3,4]
    
    nameTir = ['A','B','C','D']
    Damage = [1,1.5,3,2]
    

    
    def set_gun_by_name(self, name: str) :
        if name in self.Guns:
            self.name = name
        else:
            return Exception
        

    def add_bullet_of_given_size_to_gun(self, size: float, count: int) -> None:

        if self.name == None:
            return Exception
        elif self.Guns.index(self.name) != self.SizeTir.index(size):
            return Exception
        elif count< 0:
            return Exception
        elif size not in self.SizeTir:
            return Exception
        else:
            self.nametir = self.nameTir[self.SizeTir.index(size)] 
            self.numbertir = count    

    def shoot_to_target(self, target_x: int,  target_y: int,  target_distance: int,  aim_x: int,  aim_y: int) -> float:

        if self.Board[self.Guns.index(self.name)] < target_distance:
            return 0
        elif self.name == None or self.numbertir == 0:
            return Exception
        else:
            return self.Power[self.Guns.index(self.name)]*self.Damage[self.Guns.index(self.name)]

