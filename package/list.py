# program to do operations on the list
print("Program to do operations on the given n numbers ")
a = int(input("Enter number of number to operation done: "))

b = []

for i in range(0, a):
    c = int(input("Enter number: "))
    b.append(c)

d = b[0]
for i in range(1, a):
    if(d > b[i]):
        d = b[i]
    else:
        continue

print("The max number in the array is: ", d)
e = 0
for i in range(0, a):
    if(e < b[i]):
        e = b[i]
    else:
        continue

print("The min number in the array is: ", e)

sum = 0
for i in range(0 , a):
    sum = sum + b[i]

print("The sum of the numbers in the list is: ", sum)

avg = 0
for i in range(0 , a):
    avg = avg + b[i]
    avg = avg/a

print("The avg of the numbers in the list is: ", avg)