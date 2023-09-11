import random

class YaHaySuficientes(Exception):
    pass

class Tile:
    def __init__(self, letter, value, cant):
        self.letter = letter
        self.value = value
        self.cant = cant

class BagTiles:
    def __init__(self):
        self.tiles = {"A":Tile("A",1,12), "B":Tile("B",3,2), "C":Tile("C",3,4), "D":Tile("D",2,5), "E":Tile("E",1,12),
                    "F": Tile("F",4,1), "G":Tile("G",2,2), "H":Tile("H",4,2), "I":Tile("I",1,6), "J":Tile("J",8,1),
                    "L":Tile("L",1,4), "M":Tile("M",3,2), "N":Tile("N",1,5), "Ñ":Tile("Ñ",8,1), "O":Tile("O",1,9),
                    "P":Tile("P",3,2), "Q":Tile("Q",5,1), "R":Tile("R",1,5), "S":Tile("S",1,6), "T":Tile("T",1,4),
                    "U":Tile("U",1,5), "V":Tile("V",4,1), "X":Tile("X",8,1), "Y":Tile("Y",4,1), "Z":Tile("Z",10,1),
                    "LL":Tile("LL",8,1), "RR":Tile("RR",8,1)
                    }
        self.actualizado = {"A":Tile("A",1,12), "B":Tile("B",3,2), "C":Tile("C",3,4), "D":Tile("D",2,5), "E":Tile("E",1,12),
                    "F": Tile("F",4,1), "G":Tile("G",2,2), "H":Tile("H",4,2), "I":Tile("I",1,6), "J":Tile("J",8,1),
                    "L":Tile("L",1,4), "M":Tile("M",3,2), "N":Tile("N",1,5), "Ñ":Tile("Ñ",8,1), "O":Tile("O",1,9),
                    "P":Tile("P",3,2), "Q":Tile("Q",5,1), "R":Tile("R",1,5), "S":Tile("S",1,6), "T":Tile("T",1,4),
                    "U":Tile("U",1,5), "V":Tile("V",4,1), "X":Tile("X",8,1), "Y":Tile("Y",4,1), "Z":Tile("Z",10,1),
                    "LL":Tile("LL",8,1), "RR":Tile("RR",8,1)
                    }
    def take(self):
        letras = list(self.tiles.keys())
        elec = random.choice(letras)
        (self.actualizado[elec].cant) -= 1
        return(elec)

    def put(self, letra):
        if self.actualizado[letra].cant < self.tiles[letra].cant:
            (self.actualizado[letra].cant) += 1