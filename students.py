import csv

name= input("whats ur name ? ")
home= input("whats your home ? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"]) #function from csv module
    writer.writerow({"home" : home, "name": name})
    
        