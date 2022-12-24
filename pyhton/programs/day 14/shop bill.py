#Person visits a dress shop where 25% of discount sales was ON.
#Take user input for how many pieces of dresses purchased and the original price of each dress purchased, 
#calculate the total and discounted price and print with proper output format.
#Use classes and objects.

class shop:
    count=0
    total=0
    def __init__(self):

        self.drs_name = ""
        self.drs_quantity= ""
        self.drs_cost = ""
        self.selling_price = ""

    def get_det(self):
        shop.count+=1
        print(f"enter detail of dress",shop.count)
        self.drs_name = input("type of dress: ")
        self.drs_quantity= int(input("number of pieces: "))
        self.drs_cost = int(input(f"cost of {self.drs_name}: "))

    def fin_price(self):
        self.selling_price = .75 * self.drs_cost * self.drs_quantity
        shop.total+= self.selling_price

    def bill(self):
        print(f"{self.drs_name}\t{self.drs_quantity}\t{self.drs_cost}\t{self.selling_price}")



items_purchased=[]

n=int(input("number of items purchased: "))
for i in range(n):
    drs=shop()
    items_purchased.append(drs)
    items_purchased[i].get_det()
    items_purchased[i].fin_price()

for i in items_purchased:
    i.bill()
print("Total bill: ",shop.total)
    
