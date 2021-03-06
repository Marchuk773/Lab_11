from tools.main.models.abstract_tool import AbstractTool


class Saw(AbstractTool):
    
    def __init__(self, price_in_dollars, name, weight_in_kilos=2, length_in_centimetres=4, color="brown",
                 is_stainless=True):
        super().__init__(price_in_dollars, name, weight_in_kilos, color, is_stainless)
        self.length = length_in_centimetres
    
    def __str__(self):
        return super().__str__() + ", length = %s cm" % self.length
