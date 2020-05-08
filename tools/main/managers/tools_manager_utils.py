from tools.main.managers.sort_type import SortType
from tools.main.models.axe import Axe
from tools.main.models.saw import Saw
from tools.main.models.scissors import Scissors


class ToolsManagerUtils:
    
    @staticmethod
    def sort_by_name(given_list, sort_type=SortType.ASC):
        """
        >>> tools_list = [Axe(70, "axe"), Scissors(50, "scissors"), Saw(30, "saw")]
        >>> ToolsManagerUtils.sort_by_name(tools_list)
        >>> print(tools_list[0].name)
        axe
        >>> print(tools_list[1].name)
        saw
        >>> print(tools_list[2].name)
        scissors
        """
        given_list.sort(key=lambda tool: tool.name, reverse=(sort_type == SortType.DES))
    
    @staticmethod
    def sort_by_price(given_list, sort_type=SortType.ASC):
        """
        >>> tools_list = [Axe(70, "axe"), Saw(30, "saw"), Scissors(50, "scissors")]
        >>> ToolsManagerUtils.sort_by_price(tools_list, sort_type=SortType.DES)
        >>> print (tools_list[0].price)
        70
        >>> print(tools_list[1].price)
        50
        >>> print(tools_list[2].price)
        30
        """
        given_list.sort(key=lambda tool: tool.price, reverse=(sort_type == SortType.DES))
    
    @staticmethod
    def sort_by_weight(given_list, sort_type=SortType.ASC):
        """
        >>> tools_list = [Axe(40, "axe", 5), Saw(30, "saw", 7), Scissors(50, "scissors", 2)]
        >>> ToolsManagerUtils.sort_by_weight(tools_list)
        >>> print(tools_list[0].weight)
        2
        >>> print(tools_list[1].weight)
        5
        >>> print(tools_list[2].weight)
        7
        """
        given_list.sort(key=lambda tool: tool.weight, reverse=(sort_type == SortType.DES))


if __name__ == '__main__':
    import doctest
    
    doctest.testmod(verbose=True)
