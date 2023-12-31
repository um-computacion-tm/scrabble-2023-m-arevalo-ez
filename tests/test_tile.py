import unittest
from game.tile import (
    BagTiles,
    Tile,
)
from unittest.mock import patch

class TestTiles(unittest.TestCase):
    def test_tile1(self):
        tile = Tile('A', 1)
        self.assertEqual(tile.letter, 'A')
        self.assertEqual(tile.value, 1)

    def test_tile2(self):
        tile = Tile('H', 4)
        self.assertEqual(tile.letter, 'H')
        self.assertEqual(tile.value, 4)

    def test_tile3(self):
        tile = Tile('Z', 10)
        self.assertEqual(tile.letter, 'Z')
        self.assertEqual(tile.value, 10)

    def test_tile4(self):
        tile = Tile('LL', 8)
        self.assertEqual(tile.letter, 'LL')
        self.assertEqual(tile.value, 8)
    


class TestBagTiles(unittest.TestCase):
    @patch('random.shuffle')
    def test_bag_tiles(self, patch_shuffle):
        bag = BagTiles()
        self.assertEqual(
            len(bag.tiles),
            28,
        )
        self.assertEqual(
            patch_shuffle.call_count,
            1,
        )
        self.assertEqual(
            patch_shuffle.call_args[0][0],
            bag.tiles,
        )


    def test_take(self):
        bag = BagTiles()
        tiles = bag.take(2)
        self.assertEqual(
            len(bag.tiles),
            26,
        )   
        self.assertEqual(
            len(tiles),
            2,
        )

    def test_put(self):
        bag = BagTiles()
        put_tiles = [Tile('Z', 1), Tile('Y', 1)]
        bag.put(put_tiles)
        self.assertEqual(
            len(bag.tiles),
            30,
        )


if __name__ == '__main__':
    unittest.main()