# type of arguements in functions

def func1(num1 , num2 , num3):
    print("The 1st number is ",num1)
    print("The 2nd number is ",num2)
    print("The 3rd number is ",num3)
    print("The sum of all the numbers is ", (num1+num2+num3))
    print("\n")
    
def func2(a, b = 0):
    print("The multiplication of ",a ," ", b," is ", (a*b))
    print("\n")

def func3(name , *fav_sub):
    print(name,"'s favourite subjects are: ")
    for ele in (fav_sub):
        print(ele, end=" ")
        print("\n")
        
func1(45, 60, 90)   #req arg
func1(num3 = 90, num2 = 60 , num1 = 120)    #keyword args
func2(10 , 10)  #default
func2(10)   #default
func3("devin" , "maths" , "physics", "geography", "English" ,)  #variable args

func3("sus" , "English" , "History")    #variable args