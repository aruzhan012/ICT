a = int(input("Enter a four digit numbers: "))
b  = a // 1000
b1 = (a - b*1000) // 100
b2 = (a - b*1000 - b1*100)  //10
b3 = a - b*1000 - b1*100 - b2*10
print("The sum of digits in the number is", b+b1+b2+b3)