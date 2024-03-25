from char_creation import charcreation

from duel_round import duelround

charcreation.character_creation()

def duel_progression(self):
    while not any(char_status["death"] for char_status in self.character.characters.values()):
        duelround.add_round()