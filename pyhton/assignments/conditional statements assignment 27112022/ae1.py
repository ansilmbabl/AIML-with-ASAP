#1.A shop will give discount of 10% if the cost of purchased quantity is more than 1000.Ask user for quantity. Suppose, one unit will cost 100.Judge and print total cost for user.

q = int(input("enter the quantity: "))
d = .1
c = 100

if (q*c) > 1000:
    tc = (q*c) - d*(q*c)
else:
    tc = (q*c)

print("total cost = Rs.",tc)
