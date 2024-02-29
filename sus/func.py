b = ["1 add" , "2 sub" , "3 mult" , "4 div"]
for i in range (len(b)):
    print (b[i])
    
a = int(input("What operation u want to do "))

c = int(input("Enter the 1st number: "))
d = int(input("Enter the 2nd number: "))

def sum(a , b):
    print("sum of the given number is " , a+b)
    
def sub(a , b):
    if(a>b):
        c = a - b
    else:
        c = b - a
    print("subtraction of the given number is " , c)
def mult(a , b):
    print("multiplication of the given number is " , a*b)
    
def div(a , b):
    print("division of the given number is " , a/b)
    
if(a == 1):
    sum(c, d)
if(a == 2):
    sub(c, d)
if(a == 3):
    mult(c, d)
if(a == 4):
    div(c, d)
