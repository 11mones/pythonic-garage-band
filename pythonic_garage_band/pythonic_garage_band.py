
class Musician :

    def __init__(self , name):
        self.name = name
    def __str__(self):       
        return f"My name is {self.name} and I play {self.get_instrument()}"

    def __repr__(self):       
        return f"{self.__class__.__name__} instance. Name = {self.name}" 

class Guitarist (Musician):

    def get_instrument(self):
        return "guitar"
    def play_solo(self):
        return "face melting guitar solo"


class Drummer (Musician):

    def get_instrument(self):
        return "drums"
    
    def play_solo(self):
        return "rattle boom crash"


class Bassist (Musician):

    def get_instrument(self):
        return "bass"
    def play_solo(self):
        return "bom bom buh bom"


class Band (Musician) : 
    bands = []
    solos = []
    all_bands = []

    
    def __init__(self , name , members = [] , solos = [] , all_bands = []):
        self.name = name
        self.members = members
        self.solos = solos
        self.all_bands = all_bands
        Band.bands.append(members)
        Band.instances.append(self)
        

    def play_solos (self):
        
        
        Band.solos.append(Guitarist.play_solo(self.name))
        Band.solos.append(Bassist.play_solo(self.name))
        Band.solos.append(Drummer.play_solo(self.name))
        return Band.solos
    

    @classmethod
    def to_list(cls):
        return cls.instances
       

    