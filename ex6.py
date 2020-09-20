meal =  float(input("Enter the meal amount:"))
tax_r = 0.15
tip_p = 0.18 
tax = meal * tax_r
tip = meal* tip_p
total_p = meal + tax + tip
print("Tax: {0:0.2f}.".format(tax))
print("Tip: {0:0.2f}.".format(tip))
print("Total price: {0:0.2f}.".format(total_p))