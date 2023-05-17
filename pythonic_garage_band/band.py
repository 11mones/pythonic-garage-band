
class Musician :
    """
    A class representing a musician.
    and every musician has a name
    and the properties is 
    __str__(): Returns a string representation of the musician.
    __repr__(): Returns a string representation of the musician instance.

    """

    def __init__(self , name):
        self.name = name
    def __str__(self):       
        return f"My name is {self.name} and I play {self.get_instrument()}"

    def __repr__(self):       
        return f"{self.__class__.__name__} instance. Name = {self.name}" 

class Guitarist (Musician):
    """
    A class representing a guitarist.
    has get instrument method witch return the instrument he plays, and play solo witch returns the solo that he can play

    """

    def get_instrument(self):
        return "guitar"
    def play_solo(self):
        return "face melting guitar solo"


class Drummer (Musician):

    """
    A class representing a drummer.
    has get instrument method witch return the instrument he plays, and play solo witch returns the solo that he can play

    """

    def get_instrument(self):
        return "drums"
    
    def play_solo(self):
        return "rattle boom crash"


class Bassist (Musician):
    """
    A class representing a bassist.
    has get instrument method witch return the instrument he plays, and play solo witch returns the solo that he can play

    """

    def get_instrument(self):
        return "bass"
    def play_solo(self):
        return "bom bom buh bom"


class Band (Musician) : 

    """A class representing a band, has :
        bands (list): A list of band members.
        solos (list): A list of solos performed by band members.
        all_bands (list): A list of all band instances.
        and play_solos() method witch returns the solos by band members and returns a list of solos and to_list() witch returns a list of all band instances.

    """


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
       

    