print("Program to find highes common factorial")

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
i = 1
c = 0
while(i<=a and i<=b):
    if(a%i==0 and b%i==0):
        c = i      
    i+=1
    
print("The HCF for the given numbers is ", c)