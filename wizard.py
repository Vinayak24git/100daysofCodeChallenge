class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("missing name")
        self.name= name

class Student(Wizard): #student class will inherit all wizard class, wizard is the superclass
    def __init__(self, name, house):
        super().__init__(name) #calling the init of wizard and passing it the value of name
        if not name:
            raise ValueError("missing name")
        self.name= name
        self.house= house #assigning instance varaibles
        
        ...
        
class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name) #calling the init of wizard and passing it the value of name
        if not name:
            raise ValueError("missing name")
        self.name= name
        self.subject= subject
        
    ...
wizard= Wizard("albus")   
student= Student("harry", "gryffindor")
professor= Professor("severus", "defence against dark arts")
   