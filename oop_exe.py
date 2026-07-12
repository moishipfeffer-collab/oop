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

#extra
#1
class MenuItem:
    def __init__(self,name,price,category):
        self.name=name
        self.price=price
        self.category=category
    def is_drink(self):
        return "drink" in self.category
    def is_cheap(self,limit):
        return self.price < limit
espresso=MenuItem("espresso",3.5,"hot drink")
muffin=MenuItem("muffin",2.0,"food")
print(espresso.is_drink())
print(espresso.is_cheap(3.0))
print(muffin.is_drink())
print(muffin.is_cheap(3.0))

#2
class Customer:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
        self.points=50
    def purchase(self,item_name, price):
        if price<=self.balance:
            print(self.balance - price)
            self.points+=10
        else:
            print(f"Not enough balance for {item_name}.")
    def redeem(self):
        if self.points>=50:
            self.balance+=5
            self.points=0
    def status(self):
        print(f"Name: {self.name} | Balance: ${self.balance} | Points: {self.points}")
noa=Customer("noa",50)
noa.purchase("bottle",20)
noa.redeem()
noa.status() 

#3
class Order:
    def __init__(self,customer_name, items):
        self.name=customer_name
        self.items=items
    def total_prep_time(self):
        total=0
        for item in self.items:
            total+=item[1]
        return total
    def ready_by(self,minutes):
        return self.total_prep_time()<=minutes
    def print_order(self):
        for item in self.items:
            print(f"item: {item[0]} | time: {item[1]}")
    def slowest_item(self):
        print("slowest:",(max(self.items, key=lambda x: x[1])[0]))
moshe=Order("moshe",[("latte",3),("sandwich",7),("smoothie",5)])
moshe.total_prep_time()
print(moshe.ready_by(10))
print(moshe.ready_by(20))
moshe.print_order()
moshe.slowest_item()

#4
class coffeeShop:
    def __init__(self,name):
        self.name=name
        self.revenue = 0.0
    def sell(self,itam_name,price):
        self.revenue+=price
        print(f"item: {itam_name}price: ${price}")
    def sell_discounted(self,item_name, price, discount):
        self.revenue+=price-discount
        print(f"item: {item_name}\nprice: {self.revenue}")
    def daily_summary(self):
        print(f"{self.name} | Daily revenue: ${self.revenue:.2f}") 
cofee=coffeeShop("the bean")
cofee.sell("coffee",15)
cofee.sell_discounted("pasta",30,5)
cofee.sell("coke",20)
cofee.sell_discounted("soop",40,7)
cofee.sell("egg",15)
cofee.daily_summary()

#5
class Drink:
    def __init__(self,name,bace_price,size):
        self.name=name
        self.bace_price=bace_price
        self.siz=size
    def final_price(self):
        if self.siz == "small":
            return self.bace_price
        elif self.siz == "medium":
            return self.bace_price*1.3
        elif self.siz == "large":
            return self.bace_price*1.6
    def describe(self):
        print(f"{self.name} ({self.siz}) ${self.final_price():.2f}")
watter=Drink("watter",3.0,"small")
watter.describe()
watter=Drink("watter",3.90,"medium")
watter.describe()
watter=Drink("watter",4.80,"large")
watter.describe()

#6
class Shift:
    def __init__(self,barista_name, start_hour, end_hour, drinks_target):
        self.name=barista_name
        self.start=start_hour
        self.end=end_hour
        self.target=drinks_target
    def duration(self):
        return self.end-self.start
    def drinks_per_hour(self):
        return self.target//self.duration()
    def is_long_shift(self):
        return self.duration()>6
    def describe(self):
        print(f"barista: {self.name} | hours: {self.duration()} | target: {self.target} | per hour: {self.drinks_per_hour()}) | long shift: {self.is_long_shift()}")
moish=Shift("moish",8,16,120)
moish.describe()

#7
class MenuItem:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def HappyHour(self,start_hour, end_hour, discount_percent):
        self.start=start_hour
        self.end=end_hour
        self.discount=discount_percent
    def is_active(self,current_hour):
        return True if self.start<=current_hour<self.end else False
    def discounted_price(self):
        return self.price*(1-self.discount/100)
hour=MenuItem("beer",20.0)
hour.HappyHour(16,18,20)
print(hour.is_active(19))
print(hour.discounted_price())

#8
class Combo:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def Combo(self, name, items, discount):
        self.combo_name=name
        self.items=items
        self.discount=discount
    def original_price(self):
        return sum(self.items)
    def combo_price(self):
        return self.original_price()-self.discount
    def savings(self):
        return self.original_price()-self.combo_price() 
    def describe(self):
        print(f"{self.combo_name} | original: {self.original_price} | combo: {self.combo_price} | savings: {self.savings}")



        

        



        
        



        

        



               


        
        



    

    

        








        
