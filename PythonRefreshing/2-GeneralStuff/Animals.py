class Animal:

    alive = True

    def eat(self):
        print("This animal is eating.")
    
    def sleep(self):
        print("This animal is sleeping.")

class Prey(Animal):
    
    def flee(self):
        print("This prey is fleeing.")

class Predator(Animal):

    def hunt(self):
        print("This predator is hunting.")
    




class Fish(Prey,Predator):

    def swim(self):
        print("This fish is swimming.")
    
    #overriding
    def sleep(self):
        print("Fish don't sleep.")
    
    
class Hawk(Predator):

    def fly(self):
        print("This hawk is flying.")

    #overriding
    def eat(self):
        print("This hawk is eating.")

    #overriding
    def hunt(self):
        print("This hawk is hunting from above.")


class Rabbit(Prey):

    def run(self):
        print("This rabbit is running.")

    #overriding
    def eat(self):
        print("This rabbit is eating.")


    