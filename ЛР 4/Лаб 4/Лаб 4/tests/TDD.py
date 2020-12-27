from main2 import *
import unittest


class SummaTest(unittest.TestCase):
    def test_summa_menu(self):
        catalog = Composite('Каталог')
        blush = Composite('Подводка')
        blush.add(Leaf('Черная', 1750))
        boxes = Composite('Наборы')
        box1 = Box1()
        box1.add_all()
        box2 = Box2()
        box2.add_all()
        boxes.add(Leaf(box1.box.list_box(), box1.box.get_sum()))
        boxes.add(Leaf(box2.box.list_box(), box2.box.get_sum()))
        paper = Leaf('Средство для снятия макияжа', 250)

        catalog.add(blush)
        catalog.add(boxes)
        catalog.add(paper)

        visitor1 = Visitor1()
        self.assertEqual(catalog.accept(visitor1), 'visitor_for_composite_new', "Should be 'visitor_for_composite_new'")


if __name__ == "__main__":
    unittest.main()

