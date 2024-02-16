class Student:  #dfining ur own class
    def __init__(self, name, house): #self is to store the name and house
        if not name: #if there is no name entered
            raise ValueError("missing name") #raise keyword used to create exceptions
        if house not in ["gryffindor", "hufflepuff", "ravenclaw", "slytherin" ]:
            raise ValueError("invalid house")
        self.name= name
        self.house=house
    def __str__(self): #it always takes 1 argument i.e self
        return f"{self.name} from {self.house}"
    
    @classmethod
    def get(cls):
        name = input("name: ") #storing attributes inside of class using .
        house= input("house: ")
        return cls(name, house)

def main():
    student= Student.get()
    print(student) #when print wants to print string it iniitates the __str__ function
    

if __name__=="__main__":
    main()