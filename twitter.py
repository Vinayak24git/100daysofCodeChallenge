import re

url = input("URL = ").strip()

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
    print(f"username: ", matches.group(1))
    
    
# (?:) means dont capture the value from this ()
# ()? means it is optional
#:= is walrus symbol,  u can check for and assign value at the same time