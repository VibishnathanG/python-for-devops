import sys

def add(a, b):
    return a+b

def mul(a, b):
    return a*b


a= float(sys.argv[1])
o= sys.argv[2]
b= float(sys.argv[3])

if o == "add":
    print(add(a, b))
elif o == "mul":
    print(mul(a, b))