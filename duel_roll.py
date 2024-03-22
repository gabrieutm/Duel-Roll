class Roll:

    def __init__(self):
        import random
        self.random = random

    def roll_initiative(self, player1, player2):
        roll_itv = self.random.randint(0, 1)
        if roll_itv == 0:
            first_turn = player1
            second_turn = player2
            print(f"\nDado: {roll_itv}.\n{player1}, você começa a rodada!")
        else:
            first_turn = player2
            second_turn = player1
            print(f"\nDado: {roll_itv}.\n{player2}, você começa a rodada!")
        return roll_itv, first_turn, second_turn

    def roll_attack(self):
        roll_atk = self.random.randint(1, 20)
        print(f"\nDado: {roll_atk}.\n")
        return roll_atk
    
roll = Roll()