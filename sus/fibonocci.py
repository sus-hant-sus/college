print("Program to show fibonocci numbers ")

a = 0
b = 1
print(a , end=", ")
for i in range(0, 100):
    c = a + b
    a = b
    b = c
    print(c ,  end=", ")


