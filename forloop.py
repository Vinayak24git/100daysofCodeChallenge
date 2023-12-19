#creating my own function
def main():
    number = get_number()
    meow(number)
    
def get_number():
    while True: 
        n = int(input("what is n ? "))
        if n > 0: 
            return n
    
def meow(n):
    for _ in range(n):
        print("meow")
#calling the main function. if u dont call the maifunction it wont work.       
main()