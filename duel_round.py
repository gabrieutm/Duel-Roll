class DuelRound:

    def __init__(self):
        from duel_roll import roll
        self.roll = roll

        from char_creation import charcreation
        self.charactercreation = charcreation

        from duel_action import duelaction
        self.duelaction = duelaction

        self.rounds = []
        self.player1 = charcreation.player1
        self.player2 = charcreation.player2
        self.rounds_max = 30
        self.round_current = 0

    def round_current_turn(self, player):
        roll_result, first_player, second_player = self.roll.roll_initiative(self.player1, self.player2)
        self.duelaction.duel_action_choices(first_player)
        self.duelaction.duel_action_choices(second_player)

    def round_register(self, roll_result, first_turn, second_turn):
        
        while self.rounds_max < 30:
            roll_result, first_turn, second_turn = self.roll.roll_initiative(self.player1, self.player2)

            self.round_current += 1

            self.rounds.append({
            'round': self.round_current,
            'roll_result': roll_result,
            'first_turn': first_turn,
            'second_turn': second_turn})

duelround = DuelRound()

#ideia
"""
def round:
    roll_initiative
    def turn1():
        xxx
    def turn2():
        zzz
    turn1()
    turn2()
    return turn1, turn2
"""