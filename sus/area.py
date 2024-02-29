b = ["1 circle" , "2 square" , "3 rectangle" , "4 triangle"]

for i in range (len(b)):
    print (b[i])

a = int(input("which shapes area u want to find out "))


def circle():
    a = int(input("Enter the radius of the circle "))
    c = ((a*2)*3.14159265359)
    print("The area of the circle is ", c)    
def sqr():
    a = int(input("Enter the length of the side: "))
    print("The area of the square is ", a*a)
def rect():
    a = int(input("Enter the length of the rectangle: "))
    b = int(input("Enter the height of the rectangle: "))
    print("area of the rectangle is " , a*b)
    
def tri():
    a = int(input("Enter the base of the triangle: "))
    b = int(input("Enter the height of the triangle: "))
    print("area of the triangle is " , a*b/2)
    
if(a == 1):
    circle()
if(a == 2):
    sqr()
if(a == 3):
    rect()
if(a == 4):
    tri()