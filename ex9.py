a = int(input("The amount of money deposited into the account: "))
first = a*4/100 + a
second = first + first*4/100
third = second + second*4/100
print("The amount in the savings account after 1 years: " + str(int(first)))
print("The amount in the savings account after 2 years: " + str(int(second)))
print("The amount in the savings account after 3 years: " + str(int(third)))
