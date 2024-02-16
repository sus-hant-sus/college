print("Program to check result of student")

a = int(input("Enter  marks English subject: "))
b = int(input("Enter  marks Hindi subject: "))
c = int(input("Enter  marks Maths subject: "))
d = int(input("Enter  marks Science subject: "))
e = int(input("Enter  marks History subject: "))
f = ((a+b+c+d+e) / 500)*100
if(a < 40 or b < 100 or c < 100 or d < 100 or e < 100 )
    if(a >= 40 and b >= 40 and c >= 40 and d >= 40 and e >= 40 ):
        print("Student has obtained total of ", f ,"percentage average")
        if f>= 75:
            print("Student passed in Distinction")
            

        elif(f>=60):
            print("Student passed in first class")
        
        elif f>=50:
            print("Student passed in second class")

        else:
            print("Student passed in pass class")

    else:
        print("Student is failed.")