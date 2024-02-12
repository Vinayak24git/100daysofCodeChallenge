import re 

email= input("what is your email ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE): # ? makes whats inside () optional
    #(\w+\.) means any word or number with . basically for subdomain
    print("valid")
else:
    print("invalid")