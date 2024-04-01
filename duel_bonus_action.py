class DuelBonusAction:

    def __init__(self) -> None:
        from char_skill_natability import skillnat
        self.skillnat = skillnat

    

    def duel_bonusaction_choices(self, player, enemy, menu):

        self.bonusaction_groups = {1: 'Habilidade Natural'}
        
        while True:

            print("Opções de ações bônus: ")
            
            for key, value in self.bonusaction_groups.items():
                print(f"{key} - {list(value.keys())[0]}")

            choice = int(input("Escolha digitando o respectivo número da ação bônus (ou 0 a qualquer momento para voltar ao menu anterior): "))

            if choice == 0:
                menu(player)

            elif choice in self.bonusaction_groups.keys():

                if choice == 1:

                    while True:
                        
                        print("Opções de habilidade natural: ")
                        break


duelbonusaction = DuelBonusAction()