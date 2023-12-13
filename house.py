name = input("whats your name")

match name:
    case "harry" | "hermione" | "ron" :
        print("griffindor")
    case "draco" :
        print("slytherin")
    case _:
        print("kaun hai be?")