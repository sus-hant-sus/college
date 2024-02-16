print("Program to show n even numbers ")

a = 1
count = 0

while(a< 100):
    if(a % 2 == 0):
        print(a, end=", " )
        count+=1
    a+=1
    
print("\nThe total number of even number is ",count)
