# q1_sg7_balingkilat_maglaya.py
class Glassware:
    def __init__(self,name='glassware'):
        self.name = name
        print(f"\n{self.name} has been created and is existing.")
    def functions(self):
        print(f"This {self.name} holds nothing.")

class Beaker(Glassware):
    def __init__(self,name="Beaker"):
        super().__init__(name) #executes inheritance of child (Beaker) to parent (Glassware)
        print("It is used to hold, mix and heat liquids.")
    def __del__(self):
        print(f"{self.name} is gone")

class Tray:
    def __init__(self):
        self.glassware = Glassware("Glassware") # executes functions in class Glassware
        self.beaker = [Beaker(f"Beaker {i+1}") for i in range(5)] # creates 5 beakers
        print("\nTray is created")
    def exists(self):
        print("Glassware is existing (uses .exists() function).")
    def __del__(self):
        del self.beaker
        print("\nTray is deleted")

labGlass = Tray()
labGlass.exists()
del labGlass
