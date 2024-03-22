class Duel:

    def __init__(self):
        from character import character
        self.character = character

        from duel_roll import roll
        self.roll = roll

    def duel_action(self):
        duel_action_next_id =+ 1
        

    def duel_bonus_action(self):
        pass

    def duel_progression(self):
        while not any(char_status["death"] for char_status in self.character.characters.values()):
            self.roll.roll_initiative(self, self.character.player1, self.character.player2)
