from abc import ABC, abstractmethod

#1
class DeliveryMethod(ABC):
    @abstractmethod
    def deliver(self,order_id):
        pass
class BikeDelivery(DeliveryMethod):
    def deliver(self,order_id):
        print(f"order {order_id} delivered by bike")
bike=BikeDelivery()
bike.deliver(101)

#2
class DeliveryMethod(ABC):
    @abstractmethod
    def deliver(self,order_id):
        pass
class DroneDelivery(DeliveryMethod):
    def deliver(self,order_id):
        print(f"order {order_id} dropped by drone at your door.")
class CarDelivery(DeliveryMethod):
    def deliver(self,order_id):
        print(f"Order {order_id} brought to your building by car") 
dron=DroneDelivery()
car=CarDelivery()
dron.deliver(202)
car.deliver(202)

#3
class DeliveryMethod(ABC):
    def __init__(self,company_name):
        self.company=company_name
    @abstractmethod
    def deliver(self,order_id):
        pass
class BikeDelivery(DeliveryMethod):
    def __init__(self, company_name):
        super().__init__(company_name)
    def deliver(self,order_id):
        print(f"[{self.company}] order {order_id} - bike delivery.")

class DroneDelivery(DeliveryMethod):
    def __init__(self, company_name):
        super().__init__(company_name)
    def deliver(self,order_id):
        print(f"[{self.company}] order {order_id} - by drone.")
moishi=BikeDelivery("moishi")
rachel=DroneDelivery("rachel")
moishi.deliver(303)
rachel.deliver(303)

#4
class DeliveryMethod(ABC):
    @abstractmethod
    def deliver(self,order_id):
        pass
    @abstractmethod
    def get_eta(self):
        pass
class BikeDelivery(DeliveryMethod):
    def deliver(self,order_id):
        print(f"{order_id} is deliverd by a bike this time.")
    def get_eta(self):
        return 30
class DroneDelivery(DeliveryMethod):
    def deliver(self,order_id):
        print(f"{order_id} is deliverd by a drone this time.")
    def get_eta(self):
        return 15
ext=BikeDelivery()
nam=DroneDelivery()
nam.deliver(1)
print(nam.get_eta())
ext.deliver(1)
print(ext.get_eta())

#5
class DeliveryMethod(ABC):
    @abstractmethod
    def deliver(self,order_id):
        pass
class BrokenDelivery(DeliveryMethod):
    def deliver(self,order_id):
        print(f"order {order_id} - broken delivery")
moishi=BrokenDelivery()
moishi.deliver(10)

#6
class DeliveryFee:
    @staticmethod
    def calculate(distance_km, rate_per_km):
        return distance_km*rate_per_km
    @staticmethod 
    def with_surcharge(base_fee, surcharge_percent):
        return base_fee*(1+surcharge_percent/100)
    @staticmethod 
    def is_free(distance_km):
        return distance_km <= 2.0
print(DeliveryFee.calculate(5, 3.0))
print(DeliveryFee.with_surcharge(15.0, 10))
print(DeliveryFee.is_free(1.5))

#7
class DeliveryMethod(ABC):
    @abstractmethod
    def deliver(self,order_id):
        pass
    @abstractmethod
    def get_eta(self):
        pass
class WalkingDelivery(DeliveryMethod):
    def deliver(self,order_id):
        print(f"{order_id} by walking")
    def get_eta(self):
        return 60
class ExpressDelivery(DeliveryMethod):
    def deliver(self,order_id):
        print(f"{order_id} by express")
    def get_eta(self):
        return 10
class DeliveryHelper:
    @staticmethod 
    def faster(d1, d2):
        return d1 if d1.get_eta() <= d2.get_eta() else d2
print(f"Faster option: {DeliveryHelper.faster(WalkingDelivery(), ExpressDelivery()).__class__.__name__}")

#8
class Notifier(ABC):
    @abstractmethod
    def send(self,recipient, message):
        pass

class PushNotifier(Notifier):
    def send(self,recipient,message):
        print(f"push to {recipient}: {message}")
class WhatsAppNotifier(Notifier):
    def send(self,recipient,message):
        print(f"whtsapp to {recipient}: {message}")
class InAppNotifier(Notifier):
    def send(self,recipient,message):
        print(f"In-app banner for {recipient}: {message}")
Notifier=[PushNotifier(),WhatsAppNotifier(),InAppNotifier()]
for n in Notifier:
    n.send("customer_42", "Your order is on the way!")

#9
class Restaurant(ABC):
    @abstractmethod
    def get_menu(self):
        pass
    @abstractmethod
    def prepare_order(self,item_name):
        pass
class ItalianRestaurant(Restaurant):
    def get_menu(self):
        menu=['pasta', 'pizza', 'tiramisu']
        return menu
    def prepare_order(self,item_name):
        print(f"you ar about to get your italian {item_name}!")
class SushiRestaurant(Restaurant):
    def get_menu(self):
        menu=['maki', 'nigiri', 'ramen']    
        return menu
    def prepare_order(self,item_name):
        print(f"you ar about to get your sushi {item_name}!")
class BurgerJoint(Restaurant):
    def get_menu(self):
        menu=['burger', 'fries', 'shake']
        return menu
    def prepare_order(self,item_name):
        print(f"you ar about to get your spesial qwick {item_name}!")
for r in [ItalianRestaurant(), SushiRestaurant(), BurgerJoint()]: 
    print(r.get_menu()),
    r.prepare_order(r.get_menu()[0])

#10
class DeliveryMethod(ABC):
    @abstractmethod
    def deliver(self,order_id):
        pass
    @abstractmethod
    def get_eta(self):
        pass
    @abstractmethod
    def get_cost(self,distance_km):
        pass
class BikeDelivery(DeliveryMethod):
    def deliver(self,order_id):
        print(f"{order_id} deliverd bt bike")
    def get_eta(self):
        return 10 
    def get_cost(self,distance_km):
        return distance_km * 5
class DroneDelivery(DeliveryMethod):
    def deliver(self,order_id):
        print(f"{order_id} deliverd bt dron")
    def get_eta(self):
        return 6 
    def get_cost(self,distance_km):
        return distance_km * 10
class CarDelivery(DeliveryMethod):
    def deliver(self,order_id):
        print(f"{order_id} deliverd bt car")
    def get_eta(self):
        return 10 
    def get_cost(self,distance_km):
        return distance_km * 9
class WalkingDelivery(DeliveryMethod):
    def deliver(self,order_id):
        print(f"{order_id} deliverd by walk")
    def get_eta(self):
        return 20 
    def get_cost(self,distance_km):
        return distance_km * 4
class Platform:
    def __init__(self):
        self.delivries=[BikeDelivery(),DroneDelivery(),CarDelivery(),WalkingDelivery()]
    def cheapest_option(self,distance_km):
        cheapest_num=float("inf")
        cheapest=0
        for d in self.delivries:
            if d.get_cost(distance_km) < cheapest_num:
                cheapest_num=d.get_cost(distance_km)
                cheapest=d
        return cheapest
        
    def fastest_option(self):
        fastest_num=float("inf")
        fastest=None
        for d in self.delivries:
            if d.get_eta()<fastest_num:
                fastest_num=d.get_eta()
                fastest=d
        return fastest
        
platform = Platform()


print(f"Cheapest: {platform.cheapest_option(5.0).__class__.__name__}")
print(f"Fastest: {platform.fastest_option().__class__.__name__}")

    
    



            




    

    





              





        

    


