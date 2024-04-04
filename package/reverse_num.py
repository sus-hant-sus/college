print("Program to print n numbers in reverse")
a = int(input("Enter the number to be reversed: "))
reversed = 0
while(a != 0): #loop till a is not 0
    r = a%10 #will give last num of the given as reminder 
    reversed = reversed*10 + r  #places the last num at the highest 10s power and adds other besides it similarly
    a= a//10 #(floor value) removes the last num and updates a
    
print("The reversed number is ", reversed)