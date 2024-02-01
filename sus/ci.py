print("Program to calc compound interest")

p = int(input("Enter the principal: "))
r = int(input("Enter the ROI per annum: "))
r = (r/100)
t = int(input("Enter the tenure: "))
n = int(input("Enter how many number of times the interest is compounded annually: "))
y = ((p*(1+(r/n)))**(n*t)) 
z = y - p

print("The total amount after including interest is: ", y)
print("The total compount interest is: ", z)