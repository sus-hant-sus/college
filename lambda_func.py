#used to write a shot func in one line 

a = 10
b = 53

sum = lambda a, b : print("The sum of both the number is ", a+b )

even = lambda a : print("Even")  if(a%2 == 0) else print("odd")

max = lambda a, b: print(a) if (a>b) else print(b)

sum(a , b)
even(a)
even(b)
max(a , b)