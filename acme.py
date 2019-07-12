import random

"""
Create Product class, 
"""
class Product():
    """ACME Product Base Class"""
    def __init__(self, name, price=10, weight=20, flammability=0.5, identifier=random.randint(1000000,  9999999)):
        """Initialize properties of product class"""
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier
    
    def stealability(self):
        """Calculates the 'Stealability' factor of item and returns a human readable string"""
        stealability_factor = self.price / self.weight
        if stealability_factor < 0.5:
            return "Not so stealable..."
        elif stealability_factor >= 0.5 and stealability_factor < 1.0:
            return "Kinda stealable."
        else:
            return "Very stealable!"

    def explode(self):
        """Calculates the 'explode' factor of item and returns string representing it"""
        explosion_factor = self.flammability * self.weight
        if explosion_factor < 10:
            return "...fizzle"
        elif explosion_factor >= 10 and explosion_factor < 50:
            return "...boom!"
        else:
            return "...BABOOM!!"