class Car():
    def __init__(self):
        self.make = input("What is the make?: ")
        self.model = input("What is the model of your car?: ")
        self.year = input("What is the year of the car?: ")
        self.color = input("What is the color of the car?: ")
        self.engine = Engine()
        self.body_style = input("What is the body style?: ")
        self.top_speed = 0

    def drive(self):
        if self.engine.cyl == 8:
            self.top_speed = 120
        elif self.engine.cyl == 6:
            self.top_speed == 100
        else:
            self.top_speed = 65
        print("This car can drive")
        print("It's top speed is ",self.top_speed)
    
        
        

class Engine():
    def __init__(self):
        self.cyl = input ("How many cylinders does it have?: ")
        self.cyl_alignment = input("What is the configuration of your engine?: ")
        self.fuel_type = input("Is it gas or diesel?: ")


def main():
    my_dream_car = Car()
    my_dream_car.drive()
    
    your_car = Car()
    your_car.drive()

main()
    
    


    
