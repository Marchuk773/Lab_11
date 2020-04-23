from tools.models.abstract_tool import AbstractTool


class Scissors(AbstractTool):
    
    def __init__(self, price_in_dollars, name, type_of_scissors="for garden work", weight_in_kilos=2, color="brown",
                 is_stainless=True):
        super().__init__(price_in_dollars, name, weight_in_kilos, color, is_stainless)
        self.type = type_of_scissors
    
    def __str__(self):
        return super().__str__() + ", those scissors are %s" % self.type
