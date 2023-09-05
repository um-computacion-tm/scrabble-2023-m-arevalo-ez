import unittest
from game.xxx import calcular_valor_palabra
from game.cell import Cell
from game.tile import Tile


class TestCalculateWordValue(unittest.TestCase):
    def test_simple(self):
        word = [
            Cell(letter=Tile('C', 1)),
            Cell(letter=Tile('A', 1)),
            Cell(letter=Tile('S', 2)),
            Cell(letter=Tile('A', 1)),
        ]
        value = calcular_valor_palabra(word)
        self.assertEqual(value, 5)

    def test_with_letter_multiplier(self):
        word = [
            Cell(letter=Tile('C', 1)),
            Cell(letter=Tile('A', 1)),
            Cell(
                letter=Tile('S', 2),
                multiplier=2,
                multiplier_type='letter',
            ),
            Cell(letter=Tile('A', 1)),
        ]
        value = calcular_valor_palabra(word)
        self.assertEqual(value, 7)

if __name__ == '__main__':
    unittest.main()