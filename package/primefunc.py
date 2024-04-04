a = int(input("Enter the number to be check on: "))
flag = 0

def prime( a , flag):
    for i in range (2 , a):
        if(a%i == 0):
            flag = 1
            break

    else:
        flag = 0

    if(flag == 1):
        print("The given number is not a prime")
    elif(flag == 0 ):
        print("The given number is prime")
        
if(a >= 2):
    prime(a, flag)
elif(a == 1):
    print("1 is not a prime number")    
else:
    print("Enter number greater than 2")
    
