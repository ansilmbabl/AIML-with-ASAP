#WAP to calculate simple interest
#pnr/100
#principle amount , number of yers , rate

p = float (input("principle amount = "))
n = float (input("number of years = "))
r = float (input("rate pf interest = "))

i = p*n*r/100
print (f"simple interest = {i}")
