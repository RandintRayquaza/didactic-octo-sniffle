from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass


class Scotty(Vehicle):
    def start(self):
        print('Scotty started')
    def stop(self):
        print('Scotty stopped')
sc = Scotty()
sc.start()


class Car(Vehicle):
    def start(self):
        print('Car started')
    def stop(self):
        print('Car stopped')
c = Car()
c.start()