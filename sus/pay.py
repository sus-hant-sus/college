

print("program to calc net salary")

s = int(input("Enter base salary of the employee: "))
if(s<=0):
    print("salary shouldn't be less than or 0")
else:
    h = ((10/100)*s)
    t = ((5/100)*s)
    x = (s + h)
    y = (x + t)
    t2 = ((2/100)*y)
    total2 = (y - t2) 
    print("The base salary is: ", s)
    print("The hra is: ", h)
    print("The ta is: ", t)
    print("The tax deduction is: ", t2)

    print("The net salary is: ", total2)

