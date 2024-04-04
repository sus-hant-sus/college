def func():
    n = int(input("Enter three digit number: "))
    if(n<100 or n>999):
        print("Given number is not a three digit number")
    else:
        num = n
        rem = n%10
        n = n // 10
        rem2 = n%10
        n = n // 10
        rem3 = n%10
        arm = (rem**3 + rem2**3 + rem3**3)
        if arm == num:
            print("Armstrong number")
            
        else:
            print("Not Armstrong number")    


# func()
        