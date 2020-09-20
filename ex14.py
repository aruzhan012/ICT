a = int(input("Enter the height in centimetres: "))
inches = 2.54 * a
feet = 12 * a
b = round(inches,2)
c = round(feet,2)
print("The length in inches ", str(b))
print("The length in feet ", str(c))