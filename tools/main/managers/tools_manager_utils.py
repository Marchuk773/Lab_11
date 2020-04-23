class ToolsManagerUtils:
    
    @staticmethod
    def sort_by_name(given_list, sort_type=False):
        given_list.sort(key=lambda tool: tool.name, reverse=sort_type)
    
    @staticmethod
    def sort_by_price(given_list, sort_type=False):
        given_list.sort(key=lambda tool: tool.price, reverse=sort_type)
    
    @staticmethod
    def sort_by_weight(given_list, sort_type=False):
        given_list.sort(key=lambda tool: tool.weight, reverse=sort_type)
