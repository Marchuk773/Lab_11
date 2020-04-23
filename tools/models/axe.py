from tools.models.abstract_tool import AbstractTool


class Axe(AbstractTool):
    
    def __init__(self, price_in_dollars, name, handle_material, weight_in_kilos=2, color="brown", is_stainless=True):
        super().__init__(price_in_dollars, name, weight_in_kilos, color, is_stainless)
        self.handle_material = handle_material
    
    def __str__(self):
        return super().__str__() + ", handle is made of %s" % self.handle_material
