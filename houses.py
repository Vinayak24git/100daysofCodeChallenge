students= [
    {"name":"harry", "house":"gryffindor"},
    {"name":"ron", "house":"gryffindor"},
    {"name":"hermione", "house":"gryffindor"},
    {"name":"drako", "house":"slytherin"},
]

houses= set() #to filterout the duplicates
for student in students:
    houses.add(student["house"]) #for dict it is append, for set it is add
    #adding the names of house to the houses in the above code
    
for house in sorted(houses):#to sort the houses alphabetically
    print(house)