import unittest

from iterator import *

class IteratorTest(unittest.TestCase):
    def test_simple_iteration(self):
        collection = ListConcreteCollection()
        collection.add_item("abc")
        collection.add_item("bca")
        collection.add_item("bac")
        collection.add_item("zyx")
        collection.add_item("xyz")
        self.assertEqual(", ".join(collection), "abc, bca, bac, zyx, xyz")


if __name__ == "__main__":
    unittest.main()
