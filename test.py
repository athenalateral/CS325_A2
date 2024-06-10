# Abstract base classes
from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def arrive_at_work(self):
        pass

class Manager(Employee):
    def arrive_at_work(self):
        print("Arriving at job headquarters!")

class Supervisor(Employee):
    def arrive_at_work(self):
        print("Reporting for duty at job job!")

Isaac = Manager()
Clark = Supervisor()

Isaac.arrive_at_work()
Clark.arrive_at_work()
