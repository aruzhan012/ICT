l = int(input("How many 1 litre bottles do you have?"))
m = int(input("How many more than 1 litre bottles do you have?"))
l_dep = 0.10
m_dep = 0.25
refund = l*l_dep + m*m_dep 
a = round(refund,2)
print('The refund amount you are getting is ' + str(a) + '.')