a = []
b = []
c = []
n = int(input("Enter the total number of the numbers you want to check: "))

for i in range(n):
    x = int(input())
    a.append(x)
    
for i in range(n):
    d=a[i]
    if(d % 2 == 0):
        b.append(d)
    else:
        c.append(d)
print("Even number from the given list are: ")
for i in range (len(b)):
    print(b[i], end=", ")

print("\nOdd number from the given list are: ")
for i in range (len(c)):
    print(c[i], end=", ")   