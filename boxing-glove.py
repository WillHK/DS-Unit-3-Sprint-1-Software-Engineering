from acme import Product
from random import randint
class BoxingGlove(Product):
    def __init__(self, name, price=10, weight=10, flammability=0.5, identifier=randint(1000000,  9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier
    
    def explode(self):
        return "...it's a glove."

    def punch(self):
        if self.weight < 5:
            return "That tickles."
        elif self.weight >= 5 and self.weight < 15:
            return "Hey that hurt!"
        else:
            return "OUCH!"