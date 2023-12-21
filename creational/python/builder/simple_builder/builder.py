# Product
class Pizza:
    def __init__(self, inches):
        self.inches = inches
        self.ingredientes = ["salsa de tomate", "queso"]

    def __str__(self):
        return f'Mi pizza es de {self.inches}" con los siguientes ingredientes: {", ".join(self.ingredientes[:-1])} y {self.ingredientes[-1]}'

# Concrete Builder (Builder)
class PizzaBuilder():
    
    def __init__(self, inches):
        self.pizza = Pizza(inches)

    def addCheese(self):
        self.pizza.ingredientes.append("doble queso")

    def addPepperoni(self):
        self.pizza.ingredientes.append("pepperoni")

    def addSalami(self):
        self.pizza.ingredientes.append("salami")

    def addPimientos(self):
        self.pizza.ingredientes.append("pimientos")

    def addCebolla(self):
        self.pizza.ingredientes.append("cebolla")

    def addChampiñones(self):
        self.pizza.ingredientes.append("champiñones")

    def build(self):
        return self.pizza
    
    def reset(self):
        self.pizza.ingredientes = ["salsa de tomate", "queso"]