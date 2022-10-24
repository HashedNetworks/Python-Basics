import math
import random

# Se initiliza con la letra que el jugador seleccione, ya sea X o 0.
class Player:
    def __init__(self, letter):
        self.letter = letter

    # Queremos que todo los jugadores "get their next move"
    def get_move(self, game):
        pass

class RamdomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        pass