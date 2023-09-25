from abc import ABC, abstractmethod

class Animal(ABC):

    alive = True

    @abstractmethod
    def eat(self):
        pass
    
    def sleep(self):
        print("This animal is sleeping.")
        return self

class Prey(Animal):
    
    def flee(self):
        print("This prey is fleeing.")
        return self

class Predator(Animal):

    def hunt(self):
        print("This predator is hunting.")
        return self
    




class Fish(Prey,Predator):

    def swim(self):
        print("This fish is swimming.")
        return self
    
    def eat(self):
        print("This fish is eating.")
        return self
    
    #overriding
    def sleep(self):
        print("Fish don't sleep.")
        return self
    
    
class Hawk(Predator):

    def fly(self):
        print("This hawk is flying.")
        return self

    #overriding
    def eat(self):
        print("This hawk is eating.")
        return self

    #overriding
    def hunt(self):
        print("This hawk is hunting from above.")
        return self


class Rabbit(Prey):

    def run(self):
        print("This rabbit is running.")
        return self

    #overriding
    def eat(self):
        print("This rabbit is eating.")
        return self


    