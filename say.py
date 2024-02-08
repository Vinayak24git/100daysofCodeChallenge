import cowsay
import sys

if len(sys.argv) == 2: # name of program + user input, then it will print. 
    cowsay.trex("hello, " ,sys.argv[1])