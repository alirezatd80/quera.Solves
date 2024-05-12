class Shooter:
    
    Guns = ['Submachine Gun','Assault Rifle','Pistol','Shotgun','Sniper Rifle']
    Board  = [100,200,80,50,1000]
    Power = [10,20,8,40,30]
    
    SizeTir = [0.5,1,0.5,3,4]
    
    nameTir = ['A','B','C','D','E']
    Damage = [1,1.5,1,3,2]
    

    
    def set_gun_by_name(self, name: str) :
        if name not in self.Guns:
            return Exception
        else:
            self.name = name
           
        

    def add_bullet_of_given_size_to_gun(self, size: float, count: int) -> None:

        if self.name == None:
            return Exception
        elif count< 0:
            return Exception
        elif self.Guns.index(self.name) != self.SizeTir.index(size) and self.Guns.index(self.name) != self.SizeTir.index(size,1):
            return Exception
        
        elif size not in self.SizeTir:
            return Exception
        else:
            self.nametir = self.nameTir[self.SizeTir.index(size)] 
            self.numbertir = count    

    def shoot_to_target(self, target_x: int,  target_y: int,  target_distance: int,  aim_x: int,  aim_y: int) -> float:
        if self.name == None or self.numbertir == 0:
            return Exception
        elif self.Board[self.Guns.index(self.name)] < target_distance or aim_x-target_x>10 or aim_y-target_y>10 or aim_x-target_x<0 or aim_y-target_y<0:
            return 0
        else:
            return self.Power[self.Guns.index(self.name)]*self.Damage[self.Guns.index(self.name)]




shooter = Shooter()
shooter.set_gun_by_name('Assault Rifle')
shooter.add_bullet_of_given_size_to_gun(1, 1)
result = shooter.shoot_to_target(1, 1, 20, 5, 4)
print(result)
