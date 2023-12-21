import unittest

from adapter import *

class AdapterTest(unittest.TestCase):
    def test_round_peg_fits(self):
        hole = RoundHole(5)
        round_peg = RoundPeg(4)
        self.assertEqual(True, hole.fits(round_peg))
    
    def test_square_peg_fits(self):
        hole = RoundHole(5)
        square_peg = SquarePeg(4)
        self.assertEqual(False, hole.fits(square_peg))
    
    def test_adapted_square_peg(self):
        hole = RoundHole(5)
        square_peg = SquarePeg(4)
        square_peg_adapter = SquarePegAdapter(square_peg)
        self.assertEqual(True, hole.fits(square_peg_adapter))


if __name__ == "__main__":
    unittest.main()
