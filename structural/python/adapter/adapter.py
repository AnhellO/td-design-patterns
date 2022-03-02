import math

class RoundPeg:
    def __init__(self, radius: int) -> None:
        self.__radius = radius
    
    def get_radius(self) -> int:
        return self.__radius

class SquarePeg:
    def __init__(self, width: int) -> None:
        self.__width = width
    
    def get_width(self) -> int:
        return self.__width

class SquarePegAdapter(RoundPeg):
    def __init__(self, square_peg: SquarePeg) -> None:
        self.__square_peg = square_peg
        
    def get_radius(self) -> int:
        return (self.__square_peg.get_width() * math.sqrt(2)) / 2

class RoundHole:
    def __init__(self, radius: int) -> None:
        self.__radius = radius
    
    def get_radius(self) -> int:
        return self.__radius
        
    def fits(self, peg: RoundPeg) -> bool:
        if getattr(peg, 'get_radius', None) == None:
            return False

        if peg.get_radius() < self.__radius:
            return True
    
        return False