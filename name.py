import sys

if len(sys.argv) <2:
    sys.exit("to few arguments")
for arg in sys.argv[1:]:
    print("hello my name is ", arg)    