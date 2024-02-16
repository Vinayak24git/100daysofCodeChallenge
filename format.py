import re 

name= input("whats your name ? ")
matches= re.search(r"^(.+), (.+)$", name)
if matches:
    name= matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")

#line 4, () is used to capture
# re.search is used to capture user input
#line 6, asked the variable matches to pass the group value of ()
#into name
#group 1 is 1st parenthesis and group 2 is value of 2nd ()