nickel =5
dime = 10
quarter = 25
loonie = 100
toonie = 200

cents = int(input())
print("",cents // toonie, " toonies")
cents = cents % toonie
print("",cents // loonie, " loonies")
cents = cents % loonie
print("",cents // quarter, " quarters")
cents = cents % quarter
print("",cents // dime, " dimes")
cents = cents % dime

print("",cents // nickel, " nickels")
cents = cents % nickel


print("",cents,"pennies")


