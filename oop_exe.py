#1
class MenuItem:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def describe(self):
        print(f"Item: {self.name} | Price: ${self.price}")
coffee=MenuItem("espresso","3.5")
coffee.describe()

#2
class Customer:
    def __init__(self,name,favorite_drink):
        self.name=name
        self.fav_drink=favorite_drink
    def greet(self):
        print(f"Hi! I am {self.name} and I would like a {self.fav_drink}")
alice=Customer("alice","latte")
alice.greet()

#3
class MenuItem:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def describe(self):
        print(f"Item: {self.name} | Price: ${self.price}")
laatte=MenuItem("latte",4.5)
Croissant=MenuItem("Croissant",2.0)
Cold_Brew=MenuItem("Cold Brew",5.0)
laatte.describe()
Croissant.describe()
Cold_Brew.describe()

#4
class Customer:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def can_afford(self,price):
        print(True) if price <= self.balance else print(False)
bob=Customer("bob",10.0)
bob.can_afford(8.0)
bob.can_afford(12.0)

#5
class MenuItem:
    def __init__(self,name,price,in_stock):
        self.name=name
        self.price=price
        self.in_stock=in_stock
    def sel(self):
        self.in_stock=False
    def restock(self):
        self.in_stock=True
    def status(self):
        print (f"{self.name} is in stock") if self.in_stock == True else print(f"{self.name} is sold out")   
breade=MenuItem("bread",2.5,True)  
breade.status()
breade.sel()
breade.status()
breade.restock()
breade.status()

#6
class CoffeeShop:
    def __init__(self,name,city,capacity):
        self.name=name
        self.city=city
        self.capacity=capacity
    def open_shop(self):
        print(f"{self.name} is now open in {self.city}! capacity: {self.capacity} seats.")

    def close_shop(self):
        print(f"{self.name} is now closed! see you tomorrow!") 
Brew = CoffeeShop("Brew House","Tel Aviv",40)
Brew.open_shop()
Brew.close_shop()

#7
class MenuItem:
    def __init__(self,name,price):
        self.name=name
        self.price=price
        self.order_count = 0
    def order(self):
        self.order_count+=1
        print(f"{self.name} orded.\ntotal orders: {self.order_count}")
Cappuccino=MenuItem("Cappuccino", 4.0)
Cappuccino.order()
Cappuccino.order()
Cappuccino.order()

#8
class Orders:
    def __init__(self,customer_name, items):
        self.name=customer_name
        self.items=items
    def item_count(self):
        return len(self.items) 
    def print_order(self):
        print(f"Order for: {self.name}")
        print(f"Items: {self.item_count()}")
        for i in range(len(self.items)):
            print(f"-{self.items[i]}")
dana=Orders("dana",["latte","croissant","OJ"])
dana.print_order()

#9
class Barista:
    def __init__(self,name,specialty):
        self.name=name
        self.specialty=specialty
        self.drinks_made = 0
    def make_drink(self,drink_name):
        print(f"{self.name} made a {drink_name}")
        self.drinks_made+=1
    def is_specialty(self,drink_name):
        if drink_name == self.specialty:
            return True
        else:
            return False
    def shift_summary(self):
        print(f"{self.name} made {self.drinks_made} drinks today.")
yossi=Barista("Yossi", "latte")
yossi.make_drink("latte")
yossi.make_drink("cofee") 
yossi.make_drink("coke") 
yossi.make_drink("kjk") 
print(yossi.is_specialty("latte"))
yossi.shift_summary() 

#10
class Receipt:
    def __init__(self,tax_rate):
        self.tax_rate=tax_rate
        self.items = []
    def add_item(self,name, price):
        self.items.append((name,price))
    def subtotal(self):
        total=0
        for item in self.items:
            total+=item[1]
        return total
    def tax_amount(self):
        return self.subtotal()*self.tax_rate
    def total(self):
        return self.subtotal()+self.tax_amount()
    def print_receipt(self):
        for item in self.items:
            print(f"-{item[0]}: ${item[1]}")
            print(f"subtotal: ${self.subtotal()}\ntax: ${self.tax_amount()}\ntotal: ${self.total()}")
moishi=Receipt(0.17)
moishi.add_item("latte",4.5)
moishi.add_item("Croissant",2.0)
moishi.add_item("Water", 1.5)
moishi.print_receipt()



    

    

        








        
