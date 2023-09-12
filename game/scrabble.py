from game.board import Board
from game.player import Player
from game.tile import BagTiles


class ScrabbleGame:
    def __init__(self, players_count: int):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players:list[Player] = []
        for _ in range(players_count):
            self.players.append(Player(bag_tiles=self.bag_tiles))
        
        self.current_player = None

    def next_turn(self):
        if self.current_player is None:
            self.current_player = self.players[0]
        else:
            #index = index del current player + 1
            #len(self.players)
            index = self.players.index(self.current_player) + 1
            self.current_player = self.players[index]

    def test_next_turn_when_player_is_not_the_first(self):
        #Validar que luego del jugador 0, le toca al jugador 1
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player = scrabble_game.players[0]

        scrabble_game.next_turn()

        assert scrabble_game.current_player == scrabble_game.players[1]

    def test_next_turn_when_player_is_last(self):
        #Suponiendo que tenemos 3 jugadores, luego del jugador 3, le toca al jugador 1
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player = scrabble_game.players[2]

        scrabble_game.next_turn()

        assert scrabble_game.current_player == scrabble_game.players[0]       
