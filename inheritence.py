class Athlete:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def introduce(self):
        print(f"{self.name} is {self.age} years old and is an athlete.")
class Swimmer(Athlete):
    def __init__(self,name,age):
        super().__init__(name,age)
tom=Swimmer("tom",22)
tom.introduce()

#2
class Athlete:
    def __init__(self,name,age,sport):
        self.name=name
        self.age=age
        self.sport=sport
    def describe(self):
        print(f"{self.name} compets in {self.sport}.")
class Runner(Athlete):
    def __init__(self,name,age):
        super().__init__(name,age,sport="runing")
        sport="runing"
sara=Runner("sara",25)
sara.describe()

#3
class Athlete:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def introduce(self):
        print(f"{self.name} is {self.age} years old and is an athlete.")

class Cyclist(Athlete):
    def __init__(self,name,age,bike_brand):
        super().__init__(name,age)
        self.bike_brand=bike_brand
    def describe_gear(self):
        print(f"cyclist {self.name} rides a {self.bike_brand}.")
moishi=Cyclist("moishi",26,"trek")
moishi.introduce()
moishi.describe_gear()

#4
class Athlete:
    def __init__(self,name,country):
        self.name=name
        self.country=country
    def greet(self):
        print(f"{self.name} represents {self.country}")
class Swimmer(Athlete):
    def __init__(self,name,country,stroke_style):
        super().__init__(name,country)
        self.stroke=stroke_style
class Runner(Athlete):
    def __init__(self,name,country,best_distance):
        super().__init__(name,country)
        self.distance=best_distance
class Cyclist(Athlete):
    def __init__(self, name, country,race_type):
        super().__init__(name, country)
        self.race=race_type
lior=Swimmer("Lior", "Israel", "freestyle")
avi=Runner("Avi", "Kenya", "marathon")
jan=Cyclist("Jan", "France", "road")
lior.greet()
avi.greet()
jan.greet()

#5
class Athlete:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def worm_up(self):
        print(f"{self.name} is worming up.")
class Gymnast(Athlete):
    def __init__(self,name,age,apparatus):
        super().__init__(name,age)
        self.apparatus=apparatus
    def compete(self):
        print(f"{self.name} is a very good {self.apparatus} gymnast") 

class Swimmer(Athlete):
    def __init__(self,name,age,stroke):
        super().__init__(name,age)
        self.stroke=stroke
    
    def compete(self):
        print(f"{self.name} is a very bad {self.stroke} swimmer") 
ana=Gymnast("Ana", 19, "rings")
ben=Swimmer("Ben", 21, "butterfly")
ana.compete()
ben.compete() 

#6
class Athlete:
    def __init__(self,name,age,years_active):
        self.name=name
        self.age=age
        self.years_active=years_active
    def experience(self):
        print(f"{self.name} has been active for {self.years_active} years")

class TeamSportPlayer(Athlete):
    def __init__(self,name,age,years_active,team_name):
        super().__init__(name,age,years_active)
        self.team=team_name
    def team_info(self):
        print(f"{self.name} plays for {self.team}")

gal=TeamSportPlayer("Gal", 28, 10, "Maccabi")
gal.experience()
gal.team_info()

#7
class Athlete:
    def __init__(self,name,sport):
        self.name=name
        self.sport=sport
        self.personal_best = None
    def set_record(self,value):
        self.personal_best = value
        return self.personal_best
    def has_record(self):
        return self.personal_best != None
class Sprinter(Athlete):
    def __init__(self,name):
        super().__init__(name,"100m sprint")
usain=Sprinter("Usain")
print(usain.set_record(10.8))
print(usain.has_record())

#8
class Athlete:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.sessions_completed = 0
    def train(self):
        self.sessions_completed+=1
    def sessions_needed(self,target):
        self.left=target - self.sessions_completed
        print(f"{self.sessions_completed} sessions completed. {self.left} more neaded.")
class Triathlete(Athlete):
    def __init__(self,name,age,discipline):
        super().__init__(name,age)
        self.discipline=discipline
    def describe(self):
        print(f"Triathlete {self.name}, age {self.age}, discipline: {self.discipline}")
dan=Triathlete("Dan", 26, "cycling")
dan.train() 
dan.train() 
dan.train() 
dan.train() 
dan.sessions_needed(10)
dan.describe()

#9
class Athlete:
    def __init__(self,name,age,position):
        self.name=name
        self.age=age
        self.position=position
    def player_card(self):
        print(f"name: {self.name}, age: {self.age}, position: {self.position}")
class BasketballPlayer(Athlete):
    def __init__(self,name,age,position,jersey_number):
        super().__init__(name,age,position)
        self.number=jersey_number
    def full_profile(self):
        self.player_card()
        print(f"jersey: #{self.number}") 
mia=BasketballPlayer("Mia", 24, "guard", 7)
moshe=BasketballPlayer("noshe", 30, "player",42)
noa=BasketballPlayer("noa", 20, "guard", 19)
mia.full_profile()
moshe.full_profile()
noa.full_profile()

#10
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def great(self):
        print(f"hi, I am {self.name}")
class Athlete(Person):
    def __init__(self,name,age,sport):
        super().__init__(name,age)
        self.sport=sport
    def train(self):
        print(f"{self.name} is training for {self.sport}") 
class ProfessionalAthlete(Athlete): 
    def __init__(self, name, age, sport,sponsor):
        super().__init__(name, age, sport) 
        self.sponser=sponsor
    def sponsor_info(self):
        print(f"{self.name} is sponsored by {self.sponser}") 
ronaldo=ProfessionalAthlete("Ronaldo", 39, "football", "Nike")
ronaldo.great()
ronaldo.train()
ronaldo.sponsor_info()
        
        

        




        

        
        
    
        

        
         

        

    


        
        



        

        
        


        
        

        
    
    
        
        
        