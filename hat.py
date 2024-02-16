import random
class Hat:

    houses = ["gryffindor", "huffleuff", "ravenclaw", "slytherin"] #class varaiable, avalable to all objects in class
    @classmethod
    def sort(cls, name): #
        print(name, "is in ", random.choice(cls.houses))
    
    

Hat.sort("harry") # this is how class method works