class DuelRound:

    def __init__(self):
        import random
        self.random = random

        from char_creation import charcreation
        self.charactercreation = charcreation
        self.characters, self.player1, self.player2 = self.charactercreation.character_creation()

        from duel_action import duelaction
        self.duelaction = duelaction

        from duel_menu import duelmenu
        self.duelmenu = duelmenu

        self.rounds = []
        self.player1 = self.player1
        self.player2 = self.player2
        self.rounds_max = 30
        self.round_current = 0



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
    


    def round_hp_check(self, players):
        still_alive = True
        
        for player in players:
            
            if self.characters[player]['current_hp'] <= 0:
                self.characters[player]['death'] = True
                still_alive = False
        
        return still_alive
            


    def round_current_turn(self, players, start_menu):
        
        def round_first_turn(player, enemy):
            return start_menu(player, enemy)
                
        def round_second_turn(player, enemy):
            return start_menu(player, enemy)
    
        while self.round_current < self.rounds_max and self.round_hp_check(players) == True:

            _, first_turn, second_turn = self.roll_initiative(self.player1, self.player2)
            
            round_first_turn(first_turn, second_turn)

            print(f"{second_turn}, sua vez!")
            
            round_second_turn(second_turn, first_turn)

            self.round_current += 1
        
        if self.round_current > self.rounds_max:
            print(f"Vida de {self.player1}: {players[self.player1]['current_hp']}\nVida de {self.player2}: {players[self.player2]['current_hp']}")

            if players[self.player1]['current_hp'] > players[self.player2]['current_hp']:
                return print(f"Terminamos o último round. {self.player1}, você é o vencedor!")
            
            elif players[self.player1]['current_hp'] < players[self.player2]['current_hp']:
                return print(f"Terminamos o último round. {self.player2}, você é o vencedor!")
            
            else:
                print(f"A vida dos dois jogadores é a mesma, portanto vamos jogar mais um round. Perderá o primeiro jogador que chegar a 0 pontos de vida ou que tiver menos pontos de vida até o final do round.")
                
                self.round_current -= 1
                
                return self.round_current_turn(players, start_menu)
        
        elif self.round_hp_check(players) == False:
            print(f"Vida de {self.player1}: {players[self.player1]['current_hp']}\nVida de {self.player2}: {players[self.player2]['current_hp']}")

            if players[self.player1]['current_hp'] > players[self.player2]['current_hp']:
                return print(f"{self.player1}, você é o vencedor!")
            
            elif players[self.player1]['current_hp'] < players[self.player2]['current_hp']:
                return print(f"{self.player2}, você é o vencedor!")
            
            else:
                print(f"A vida dos dois jogadores é a mesma, portanto vamos jogar mais um round. Perderá o primeiro jogador que chegar a 0 pontos de vida ou que tiver menos pontos de vida até o final do round.")

                players[self.player1]['current_hp'] = 1
                players[self.player1]['death'] = False
                
                players[self.player2]['current_hp'] = 1
                players[self.player2]['death'] = False

                self.round_current -= 1

                return self.round_current_turn(players, start_menu)
            


        
"""
    def round_register(self, roll_result, first_turn, second_turn):
        
        while self.rounds_max < 30:
            roll_result, first_turn, second_turn = self.roll.roll_initiative(self.player1, self.player2)

            self.round_current += 1

            self.rounds.append({
            'round': self.round_current,
            'roll_result': roll_result,
            'first_turn': first_turn,
            'second_turn': second_turn})
"""



duelround = DuelRound()



if __name__ == '__main__':
    pass