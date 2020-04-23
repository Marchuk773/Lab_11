from tools.main.managers.tools_manager_utils import ToolsManagerUtils


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
    
    def find_by_price(self, lower_price, higher_price=None):
        found_tools = []
        if higher_price is None:
            for tool in self.tools_list:
                if tool.price == lower_price:
                    found_tools.append(tool)
            return found_tools
        else:
            for tool in self.tools_list:
                if lower_price <= tool.price <= higher_price:
                    found_tools.append(tool)
            else:
                ToolsManagerUtils.sort_by_price(found_tools)
            return found_tools
    
    def find_by_name(self, name):
        found_tools = []
        for tool in self.tools_list:
            if tool.name == name:
                found_tools.append(tool)
        return found_tools
