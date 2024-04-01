class DuelMenu:

    def __init__(self):
        from duel_action import duelaction
        self.duelaction = duelaction

        from duel_bonus_action import duelbonusaction
        self.duelbonusaction = duelbonusaction

        self.duel_menu_options = {1: ('Ação', self.duelaction.duel_action_choices), 2: ('Ação Bônus', self.duelbonusaction.duel_bonusaction_choices)}



    def duel_menu_option(self, player, enemy):
        for key, value in self.duel_menu_options.items():
            print(f"{key} - {value[0]}")

        while True:
            
            duel_menu_choice = int(input(f"Digite o número da sua escolha: "))

            if duel_menu_choice in self.duel_menu_options.keys():
                return self.duel_menu_options[duel_menu_choice][1](player, enemy, self.duel_menu_option)
            
            else:
                continue



duelmenu = DuelMenu()



if __name__ == '__main__':
    pass