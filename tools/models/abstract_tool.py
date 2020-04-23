from abc import ABC, abstractmethod


class AbstractTool(ABC):
    
    def __init__(self, price_in_dollars, name, weight_in_kilos, color, is_stainless):
        self.price = price_in_dollars
        self.name = name
        self.weight = weight_in_kilos
        self.color = color
        self.is_stainless = is_stainless
    
    def __str__(self):
        return "Price = %s$, name is %s, weight = %s kilos, color is %s, the steel is stainless: %s" % (
            self.price, self.name, self.weight, self.color, self.is_stainless)
