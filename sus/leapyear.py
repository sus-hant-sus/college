print("program to check leap year")

a = int(input("Enter the year to check: "))

if((a%4) == 0) :
    print("The year", a, " is leap year")
    
else: 
    print("The year" ,a, " is not a leap year")