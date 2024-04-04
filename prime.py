flag = 0
print("Program to check if number is prime")

a = int(input("Enter number to check: "))

if a == 1 or a == 0:
    print("The given number ", a ,"is not prime number")

else:
    for i in range (2 , a):
        if (a % i == 0):
            flag = 1
            break
        else:
            flag = 0 

    if flag == 1:
        print("The given number is not a prime number")
    else:
        print("The given number is prime number")         

