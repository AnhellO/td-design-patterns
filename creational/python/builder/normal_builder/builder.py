import abc

class Car:
    def __init__(self, seats=None, engine=None, trip_computer=None, gps=None) -> None:
        self.seats = seats
        self.engine = engine
        self.trip_computer = trip_computer
        self.gps = gps
    
    def set_seats(self, seats):
        self.seats = seats

    def set_engine(self, engine):
        self.engine = engine

    def set_trip_computer(self, trip_computer):
        self.trip_computer = trip_computer

    def set_gps(self, gps):
        self.gps = gps


# Builder interface
class Builder(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def reset(self):
        pass
    
    @abc.abstractmethod
    def set_seats(self, number):
        pass
    
    @abc.abstractmethod
    def set_engine(self, engine):
        pass
    
    @abc.abstractmethod
    def set_trip_computer(self, km):
        pass
    
    @abc.abstractmethod
    def set_gps(self, has_gps):
        pass

# ConcreteBuilder1
class CarBuilder(Builder):
    def __init__(self) -> None:
        self.car = Car()

    def reset(self):
        pass

    def set_seats(self, number):
        self.car.set_seats(number)

    def set_engine(self, engine):
        self.car.set_engine(engine)

    def set_trip_computer(self, km):
        self.car.set_trip_computer(km)

    def set_gps(self, has_gps):
        self.car.set_gps(has_gps)
    
    def get_result(self):
        return self.car
