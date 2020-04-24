from tools.main.managers.tools_manager_utils import ToolsManagerUtils
from overload import overload
from tools.main.models.axe import Axe
from tools.main.models.saw import Saw
from tools.main.models.scissors import Scissors
import doctest


class ToolsManager:
    
    def __init__(self, tools_list):
        self.tools_list = tools_list
    
    def add_tool(self, tool):
        self.tools_list.append(tool)
    
    def add_tools(self, tools):
        self.tools_list += tools
    
    def print_items(self):
        print("Items in this list:")
        print(*self.tools_list, sep="\n")
    
    @overload
    def find_by_price(self, lower_price, higher_price):
        """
        Returning objects with price in range on lower_price to higher_price
        >>> print(manager.find_by_price(40)[0].price)
        40
        >>> print(manager.find_by_price(35, 55)[0].price)
        40
        >>> print(manager.find_by_price(35, 55)[1].price)
        50
        """
        found_tools = []
        for tool in self.tools_list:
            if lower_price <= tool.price <= higher_price:
                found_tools.append(tool)
        else:
            ToolsManagerUtils.sort_by_price(found_tools)
        return found_tools
    
    @find_by_price.add
    def find_by_price(self, given_price):
        """
        because of overloading this test would not work, so test is in original method
        """
        found_tools = []
        for tool in self.tools_list:
            if tool.price == given_price:
                found_tools.append(tool)
        return found_tools
    
    def find_by_name(self, name):
        """
        Finds tools by name
        >>> print(manager.find_by_name("My saw")[0].name)
        My saw
        """
        found_tools = []
        for tool in self.tools_list:
            if tool.name == name:
                found_tools.append(tool)
        return found_tools


if __name__ == '__main__':
    doctest.testmod(verbose=True, extraglobs={'manager': ToolsManager(tools_list=[Axe(40, "Super axe", 3),
                                                                                  Saw(30, "My saw", 2),
                                                                                  Scissors(50, "Gardening scissors"),
                                                                                  Saw(60, "Ultra saw", 3)])})
