#1
class Device:
    def __init__(self,name):
        self.name=name
    def activate(self):
        print(f"device {self.name} is now on.")
class SmartTV(Device):
    def __init__(self,name):
        super().__init__(name)
    def activate(self):
        print(f"TV {self.name} is playing the home screen.")
class SmartSpeaker(Device):
    def __init__(self, name):
        super().__init__(name)
    def activate(self):
        print(f"speaker {self.name} is ready to play music.")
Samsung=SmartTV("Samsung")
Echo=SmartSpeaker("Echo")              
Samsung.activate()
Echo.activate() 

#2
class Device:
    def __init__(self,name):
        self.name=name
    def deactivate(self):
        print(f"Device {self.name} is now off")
class SmartLamp(Device):
    def __init__(self, name):
        super().__init__(name)
    def deactivate(self):
        print(f"Lamp {self.name} is dimming and turning off")
class SmartAC(Device):
    def __init__(self, name):
        super().__init__(name)
    def deactivate(self):
        print(f"AC {self.name} is cooling down and switching off")
SmartLamp("Bedroom Lamp").deactivate()
SmartAC("Living Room AC").deactivate()

#3
class Device:
    def __init__(self,name,is_on):
        self.name=name
        self.is_on=is_on
    def status(self):
        print(f"{self.name}: on or {self.name}: off.")
class SmartTV(Device):
    def __init__(self, name, is_on,channel):
        super().__init__(name, is_on)
        self.channel=channel
    def status(self):
        if self.is_on:
            print(f"{self.name}: on, watching channel {self.channel}.") 
        else:
            print(f"{self.name}: off.")
class SmartSpeaker(Device):
    def __init__(self, name, is_on,song):
        super().__init__(name, is_on,) 
        self.song=song     
    def status(self):
        if self.is_on:
            print(f"{self.name}: on, playing song {self.song}.")
        else:
            print(f"{self.name}: off.")
SmartTV("LG", True, 8).status()
SmartSpeaker("Alexa", True, "Bohemian Rhapsody").status()

#4
class Device:
    def __init__(self,name):
        self.name=name
    def activate(self):
        print(f"{self.name} is very good.")
class SmartTV(Device):
    def __init__(self, name):
        super().__init__(name)
    def activate(self):
        print(f"{self.name} is not so good")
class SmartLamp(Device):
    def __init__(self, name):
        super().__init__(name)
    def activate(self):
        print(f"{self.name} is great!")
class SmartSpeaker(Device):
    def __init__(self, name):
        super().__init__(name)
    def activate(self):
        print(f"{self.name} id bad.")
devices = [SmartTV("LG"), SmartLamp("Desk Lamp"), SmartSpeaker("Echo")]
for d in devices:
    d.activate()

#5
class Device:
    def __init__(self,name):
        self.name=name
    def set_volume(self,level):
        print(f"devise {self.name} volume sets to {level}")
class SmartSpeaker(Device):
    def __init__(self, name):
        super().__init__(name)
    def set_volume(self, level):
        print(f"Speaker {self.name} is now at volume {level}/10. {'Loud!' if level > 7 else ''}")
class SmartTV(Device):
    def __init__(self, name):
        super().__init__(name)
    def set_volume(self, level):
        print(f"TV {self.name} volume: {level}. {'Muted!' if level == 0 else ''}") 
SmartSpeaker("Bose").set_volume(9)
SmartSpeaker("Bose").set_volume(3)        
SmartTV("nj").set_volume(9)
SmartTV("nj").set_volume(0)

#6
class Device:
    def __init__(self,name):
        self.name=name
    def run_command(self,cmd):
        print(f"device{self.name} received command: {cmd}.")
class SmartSpeaker(Device):
    def __init__(self, name):
        super().__init__(name)
    def run_command(self, cmd):
        print(f"device {self.name} received smart command {cmd}")
class SmartLamb(Device):
    def __init__(self, name):
        super().__init__(name)
    def run_command(self, cmd):
        print(f"device {self.name} received light command {cmd}")

class SmartAC(Device):
    def __init__(self, name):
        super().__init__(name)
    def run_command(self, cmd):
        print(f"device {self.name} received a command {cmd}")

class SmartTV(Device):
    def __init__(self, name):
        super().__init__(name)
    def run_command(self, cmd):
        print(f"device {self.name} received an on command {cmd}")
device=[SmartSpeaker("n"),SmartLamb("m"),SmartAC("p"),SmartTV("t")]
def send_command(device, cmd):
    device.run_command(cmd)
for d in device:
    send_command(d,"start")

#7
class Device:
    def __init__(self,name):
        self.name=name
    def run_schedule(self,hour):
        print(f"{self.name}: is idle.")
class SmartLamp(Device):
    def __init__(self, name):
        super().__init__(name)
    def run_schedule(self,hour):
        if 23>=hour>=12:
            print(f"{self.name}: is on.")
        else:
            print(f"{self.name}: is off.")
class SmartAC(Device):
    def __init__(self, name):
        super().__init__(name)
    def run_schedule(self,hour):
        if 12<=hour<=20:
            print(f"{self.name}: is on.")
        else:
            print(f"{self.name}: is off.")
class SmartTV(Device):
    def __init__(self, name):
        super().__init__(name)
    def run_schedule(self,hour):
        if 20<=hour<=23:
            print(f"{self.name}: is on.")
        else:
            print(f"{self.name}: is off.")
SmartLamp("desk lamb").run_schedule(21)
SmartAC("living room AC").run_schedule(21)
SmartTV("samsung TV").run_schedule(21)

#8
class Device:
    def __init__(self,name):
        self.name=name
    def energy_usage(self):
        return 10 
class SmartTV(Device):
    def __init__(self, name):
        super().__init__(name)
    def energy_usage(self):
        return 150
class SmartAC(Device):
    def __init__(self, name):
        super().__init__(name)
    def energy_usage(self):
        return 900
class SmartLamp(Device):
    def __init__(self, name):
        super().__init__(name)
    def energy_usage(self):
        return 8
class SmartSpeaker(Device):
    def __init__(self, name):
        super().__init__(name)
    def energy_usage(self):
        return 30
energy_list=[SmartTV("TV"),SmartAC("AC"),SmartLamp("desk lamb"),SmartSpeaker("speaker")]
total=0
for e in energy_list:
    print(f"{e.__class__.__name__}: {e.energy_usage()}")
    total+=e.energy_usage()
print(f"total: {total}")

#9
class Device:
    def __init__(self,name):
        
        


    
        

    



        
    


    

        

        