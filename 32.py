a=[]
for i in range(3):
    b=int(input())
    a.append(b)
a.sort()
print("The minimum value is",a[0])
print("The maximum value is",a[2])
print("The middle value is",a[1])