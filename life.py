from os import system
import random
import time

class human:
    def __init__(self) -> None:
        self.inv = []
        self.loc = "house"
        self.stress = 10
    
    def stressCheck(self):
        if self.stress>=100:
            for _ in range(3):
                time.sleep(1)
                print(".",end="")
            print("\nYou commmited suicide")
            system("exit")
            

    def touch(self,obj):
        print("touched {obj}".format())

    def find(self,obj):
        if random.randint(-5,1):
            print("found {obj}".format())
            self.inv.append(obj)

    def go(self,loc):
        print("went to {loc}".format())
        self.loc = loc

    def study(self,topic,hour):
        print("studied {topic} for {hour} hour(s)".format())
        self.stress+=hour*5
        self.stressCheck()
    
    def relax(self,hour):
        if self.loc in ["park","garden","temple"]:
            print("relaxed for {hour} hour(s)")
            self.stress-=3*hour
        
    def do_seggs(self):
        for i in ["girl","bitch","bitches","gf","girlfriend","grill"]:
            if i in self.inv:
                print("doing seggs!")
                break
        #else:
        print("ur lonely, go get bitches!")
        
        