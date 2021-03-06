import unittest

from tools.main.managers.tools_manager import ToolsManager
from tools.main.managers.tools_manager_utils import ToolsManagerUtils
from tools.main.models.axe import Axe
from tools.main.models.saw import Saw
from tools.main.models.scissors import Scissors


class ToolsManagerTest(unittest.TestCase):
    def setUp(self):
        self.first_tool = Axe(40, "Super axe")
        self.second_tool = Saw(30, "My saw")
        self.third_tool = Scissors(50, "Gardening scissors")
        self.fourth_tool = Saw(60, "Ultra saw")
        self.tools_list = [self.first_tool, self.second_tool, self.third_tool, self.fourth_tool]
        self.manager = ToolsManager(self.tools_list)


class TestFinding(ToolsManagerTest):
    def test_finding_by_price(self):
        self.assertEqual(first=self.manager.find_by_price(30), second=[self.second_tool])
        self.assertEqual(first=self.manager.find_by_price(35, 55), second=[self.first_tool, self.third_tool])
    
    def test_finding_by_name(self):
        self.assertEqual(first=self.manager.find_by_name("My saw"), second=[self.second_tool])


class TestSorting(ToolsManagerTest):
    def test_sorting_by_price(self):
        ToolsManagerUtils.sort_by_price(self.tools_list)
        self.assertEqual(first=self.tools_list[0], second=self.second_tool)
        self.assertEqual(first=self.tools_list[1], second=self.first_tool)
        self.assertEqual(first=self.tools_list[2], second=self.third_tool)
        self.assertEqual(first=self.tools_list[3], second=self.fourth_tool)
    
    def test_sorting_by_name(self):
        ToolsManagerUtils.sort_by_name(self.tools_list)
        self.assertEqual(first=self.tools_list[0], second=self.third_tool)
        self.assertEqual(first=self.tools_list[1], second=self.second_tool)
        self.assertEqual(first=self.tools_list[2], second=self.first_tool)
        self.assertEqual(first=self.tools_list[3], second=self.fourth_tool)


if __name__ == '__main__':
    unittest.main()
