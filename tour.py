from money import *

_destinations = ({ "name": "Greece", "price": Money(100,"EUR")},{ "name": "France", "price": Money(120,"EUR")}, { "name": "Italy", "price": Money(200,"EUR")}, { "name": "USA", "price": Money(300,"USD")})
class _Tour:
  def __init__(self, destination, name, tourists,period):
    self.destination = destination
    self.name = name
    self.tourists = tourists
    self.period = period  
    self.cost = self.calculateCost()
  def calculateCost(self):
    def get_amount(self):
        return self.amount
    
    for i in _destinations:
        for k in _destinations[k].key():
          money_object = _destinations[k]["price"]
          price_value = money_object.get_amount()
    cost =  price_value * self.tourists
    return cost
  
  class TourBuilder:
    def __init__(self, destination, name, tourists, period):
        self._tour = _Tour(destination, name, tourists, period)
    def withEnsurance(self):
        ensurance = True
        return self
    def withEnsurance(self):
        pass
        return self 
    def withGuide(self):
        pass
        return self        
    def build(self):
        return self._tour     