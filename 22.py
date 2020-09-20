import math
s1 = int(input("Enter the first length of the sides:"))
s2 = int(input("Enter the second length of the sides:"))
s3 = int(input("Enter the third length of the sides:"))
s = (s1 +s2 +s3)/2
area = (s*(s-s1)*(s-s2)*(s-s3))** 0.5

print("The area of a Triangle:",area)