class Car:
    
    make = None
    model = None
    year = None
    color = None
    wheels = 4 #class variable

    def __init__(self,make,model,year,color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("You drive the "+self.make+" "+self.model+".")
    
    def stop(self):
        print("You stop the "+self.make+" "+self.model+".")