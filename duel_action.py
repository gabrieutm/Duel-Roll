class DuelAction:

    def __init__(self):
        """
        from char_skill_evasion import skilleva
        self.skilleva = skilleva

        from char_skill_forceatk import skillfrcatk
        self.skillfrcatk = skillfrcatk

        from char_skill_healing import skillhln
        self.skillhln = skillhln

        from char_skill_rest import rest
        self.rest = rest

        from char_skill_simpleatk import skillsplatk
        self.skillsplatk = skillsplatk

        from char_skill_special import skillspc
        self.skillspc = skillspc
"""
        from char_creation import charcreation
        self.charactercreation = charcreation



        from duel_roll import roll
        self.roll = roll
        


        from char_skill_simpleatk import skillsplatk, skillsplatk_ethereal_burst, skillsplatk_wild_charge, skillsplatk_shadow_arrow, skillsplatk_skeleton, skillsplatk_excruciating_gaze
        
        self.skillsplatk = skillsplatk
        self.skillsplatk_ethereal_burst = skillsplatk_ethereal_burst
        self.skillsplatk_wild_charge = skillsplatk_wild_charge
        self.skillsplatk_shadow_arrow = skillsplatk_shadow_arrow
        self.skillsplatk_skeleton = skillsplatk_skeleton
        self.skillsplatk_excruciating_gaze = skillsplatk_excruciating_gaze



        from char_skill_defense import skilldef, skilldef_magic_shield, skilldef_iron_skin, skilldef_invisible_cloak, skilldef_bone_shield, skilldef_bad_and_good_luck

        self.skilldef = skilldef
        self.skilldef_magic_shield = skilldef_magic_shield
        self.skilldef_iron_skin = skilldef_iron_skin
        self.skilldef_invisible_cloak = skilldef_invisible_cloak
        self.skilldef_bone_shield = skilldef_bone_shield
        self.skilldef_bad_and_good_luck = skilldef_bad_and_good_luck


    
    def duel_action_stamina_check(self, player, action_stamina_cost):
        return self.charactercreation.characters[player]['stamina'] >= action_stamina_cost



    def duel_action_choices(self, player):

        self.action_groups = {1: {'Atacar': {1: 'Ataque Simples', 2: 'Ataque Poderoso', 3: 'Ataque Especial'}}, 2: {'Defender': {1: 'Defesa', 2: 'Evasão'}}, 3: {'Curar': {1: 'Cura', 2: 'Descanso'}}}
        
        while True:

            print("Opções de ações: ")
            
            for key, value in self.action_groups.items():
                print(f"{key} - {list(value.keys())[0]}")

            try:
                choice = int(input("Escolha digitando o respectivo número da ação (ou 0 a qualquer momento para voltar ao menu de ações): "))

            except ValueError:
                print("Entrada inválida. Por favor, insira um número da lista.")
                continue

            if choice == 0:
                continue

            elif choice in self.action_groups.keys():

                if choice == 1:

                    while True:
                        
                        print("Opções de ataque: ")
                        
                        for key, value in self.action_groups[1]['Atacar'].items():
                            print(f"{key} - {value}")
                        
                        try:
                            final_choice = int(input("Escolha digitando o respectivo número do ataque: "))
                        
                        except ValueError:
                            print("Entrada inválida. Por favor, insira um número da lista.")
                            continue
                        
                        if final_choice == 0:
                            break
                        
                        elif final_choice in self.action_groups[1]['Atacar'].keys():
                            final_choice = self.action_groups[1]['Atacar'][final_choice]
                            return final_choice
                        
                        else:
                            print("Entrada inválida. Por favor, insira um número da lista.")
                    
                    break
                
                if choice == 2:
                    
                    while True:
                        
                        print("Opções de defesa: ")
                        
                        for key, value in self.action_groups[2]['Defender'].items():
                            print(f"{key} - {value}")
                        
                        try:
                            final_choice = int(input("Escolha digitando o respectivo número da defesa: "))
                        
                        except ValueError:
                            print("Entrada inválida. Por favor, insira um número da lista.")
                            continue
                        
                        if final_choice == 0:
                            break
                        
                        elif final_choice in self.action_groups[2]['Defender'].keys():
                            final_choice = self.action_groups[2]['Defender'][final_choice]
                            return final_choice
                        
                        else:
                            print("Entrada inválida. Por favor, insira um número da lista.")
                    
                    break

                if choice == 3:
                    
                    while True:
                        
                        print("Opções de cura: ")
                        
                        for key, value in self.action_groups[3]['Curar'].items():
                            print(f"{key} - {value}")
                        
                        try:
                            final_choice = int(input("Escolha digitando o respectivo número da cura: "))
                        
                        except ValueError:
                            print("Entrada inválida. Por favor, insira um número da lista.")
                            continue
                        
                        if final_choice == 0:
                            break
                        
                        elif final_choice in self.action_groups[3]['Curar'].keys():
                            self.final_choice = self.action_groups[3]['Curar'][final_choice]
                            return final_choice
                        
                        else:
                            print("Entrada inválida. Por favor, insira um número da lista.")
                    
                    break

            else:
                print("Entrada inválida. Por favor, insira um número da lista.")
                continue
    
    def duel_action_move(self, player, enemy, final_choice):
        
        if final_choice == 'Ataque Simples':

            if self.duel_action_stamina_check(player, self.skillsplatk.skill_spl_attack_cost) == True:

                print("Opções de Ataque Simples: ")
                
                if self.charactercreation.characters[player]['class'] == 'Mago':

                    print(f"{self.skillsplatk_ethereal_burst['id_skill']} - {self.skillsplatk_ethereal_burst['name_skill']}\n{self.skillsplatk_ethereal_burst['info_skill']['skill_desc']}")

                    final_choice_confirm = input("Deseja realizar este ataque? (S/N)").upper()

                    if final_choice_confirm == 'S':
                        roll_attack = self.roll.roll_attack()

                        if roll_attack > self.charactercreation.characters[enemy]['current_armor']:
                            self.skillsplatk.skill_spl_attack_hit(player, enemy, self.skillsplatk_ethereal_burst['name_skill'], self.charactercreation.characters)
                        
                        else:
                            print(f"Você errou! (armadura do oponente: {self.charactercreation.characters[enemy]['current_armor']})")

                        return roll_attack

                    else:
                        self.duel_action_choices(player)
                        back_to_action_choices = True
                        return back_to_action_choices



                if self.charactercreation.characters[player]['class'] == 'Bárbaro':

                    print(f"{self.skillsplatk_wild_charge['id_skill']} - {self.skillsplatk_wild_charge['name_skill']}\n{self.skillsplatk_wild_charge['info_skill']['skill_desc']}")

                    final_choice_confirm = input("Deseja realizar este ataque? (S/N)").upper()

                    if final_choice_confirm == 'S':
                        roll_attack = self.roll.roll_attack()

                        if roll_attack > self.charactercreation.characters[enemy]['current_armor']:
                            self.skillsplatk.skill_spl_attack_hit(player, enemy, self.skillsplatk_wild_charge['name_skill'], self.charactercreation.characters)
                        
                        else:
                            print(f"Você errou! (armadura do oponente: {self.charactercreation.characters[enemy]['current_armor']})")

                        return roll_attack

                    else:
                        self.duel_action_choices(player)
                        back_to_action_choices = True
                        return back_to_action_choices
                    
                if self.charactercreation.characters[player]['class'] == 'Assassino':

                    print(f"{self.skillsplatk_shadow_arrow['id_skill']} - {self.skillsplatk_shadow_arrow['name_skill']}\n{self.skillsplatk_shadow_arrow['info_skill']['skill_desc']}")

                    final_choice_confirm = input("Deseja realizar este ataque? (S/N)").upper()

                    if final_choice_confirm == 'S':
                        roll_attack = self.roll.roll_attack()

                        if roll_attack > self.charactercreation.characters[enemy]['current_armor']:
                            self.skillsplatk.skill_spl_attack_hit(player, enemy, self.skillsplatk_shadow_arrow['name_skill'], self.charactercreation.characters)
                        else:
                            print(f"Você errou! (armadura do oponente: {self.charactercreation.characters[enemy]['current_armor']})")

                        return roll_attack

                    else:
                        self.duel_action_choices(player)
                        back_to_action_choices = True
                        return back_to_action_choices
                    


                if self.charactercreation.characters[player]['class'] == 'Necromante':

                    print(f"{self.skillsplatk_skeleton['id_skill']} - {self.skillsplatk_skeleton['name_skill']}\n{self.skillsplatk_skeleton['info_skill']['skill_desc']}")

                    final_choice_confirm = input("Deseja realizar este ataque? (S/N)").upper()

                    if final_choice_confirm == 'S':
                        roll_attack = self.roll.roll_attack()

                        if roll_attack > self.charactercreation.characters[enemy]['current_armor']:
                            self.skillsplatk.skill_spl_attack_hit(player, enemy, self.skillsplatk_skeleton['name_skill'], self.charactercreation.characters)
                        else:
                            print(f"Você errou! (armadura do oponente: {self.charactercreation.characters[enemy]['current_armor']})")

                        return roll_attack

                    else:
                        self.duel_action_choices(player)
                        back_to_action_choices = True
                        return back_to_action_choices
                    


                if self.charactercreation.characters[player]['class'] == 'Bruxa':

                    print(f"{self.skillsplatk_excruciating_gaze['id_skill']} - {self.skillsplatk_excruciating_gaze['name_skill']}\n{self.skillsplatk_excruciating_gaze['info_skill']['skill_desc']}")

                    final_choice_confirm = input("Deseja realizar este ataque? (S/N)").upper()

                    if final_choice_confirm == 'S':
                        roll_attack = self.roll.roll_attack()

                        if roll_attack > self.charactercreation.characters[enemy]['current_armor']:
                            self.skillsplatk.skill_spl_attack_hit(player, enemy, self.skillsplatk_excruciating_gaze['name_skill'], self.charactercreation.characters)
                        else:
                            print(f"Você errou! (armadura do oponente: {self.charactercreation.characters[enemy]['current_armor']})")

                        return roll_attack

                    else:
                        self.duel_action_choices(player)
                        back_to_action_choices = True
                        return back_to_action_choices
                    


            else:
                print(f"Você não possui vigor o suficiente ({self.charactercreation.characters[player]['stamina']}) para realizar esta ação (custo: {self.skillsplatk.skill_spl_attack_cost}).\nPor gentileza, selecione outra ação ou utilize seu turno para descansar.")
                self.duel_action_choices(player)
                back_to_action_choices = True
                return back_to_action_choices
            
            

        if final_choice == 'Ataque Poderoso':
            pass
        if final_choice == 'Ataque Especial':
            pass
        
        
        
        if final_choice == 'Defesa':

            if self.duel_action_stamina_check(player, self.skilldef.skill_def_cost) == True:

                print("Opções de Defesa: ")
                
                if self.charactercreation.characters[player]['class'] == 'Mago':

                    print(f"{self.skilldef_magic_shield['id_skill']} - {self.skilldef_magic_shield['name_skill']}\n{self.skilldef_magic_shield['info_skill']['skill_desc']}")

                    final_choice_confirm = input("Deseja realizar esta defesa? (S/N)").upper()

                    if final_choice_confirm == 'S':
                        self.skilldef.skill_defense(player, self.skilldef_magic_shield['name_skill'], self.charactercreation.characters)

                    else:
                        self.duel_action_choices(player)
                        back_to_action_choices = True
                        return back_to_action_choices
                


                if self.charactercreation.characters[player]['class'] == 'Bárbaro':

                    print(f"{self.skilldef_iron_skin['id_skill']} - {self.skilldef_iron_skin['name_skill']}\n{self.skilldef_iron_skin['info_skill']['skill_desc']}")

                    final_choice_confirm = input("Deseja realizar esta defesa? (S/N)").upper()

                    if final_choice_confirm == 'S':
                        self.skilldef.skill_defense(player, self.skilldef_iron_skin['name_skill'], self.charactercreation.characters)

                    else:
                        self.duel_action_choices(player)
                        back_to_action_choices = True
                        return back_to_action_choices
                    


                if self.charactercreation.characters[player]['class'] == 'Assassino':

                    print(f"{self.skilldef_invisible_cloak['id_skill']} - {self.skilldef_invisible_cloak['name_skill']}\n{self.skilldef_invisible_cloak['info_skill']['skill_desc']}")

                    final_choice_confirm = input("Deseja realizar esta defesa? (S/N)").upper()

                    if final_choice_confirm == 'S':
                        self.skilldef.skill_defense(player, self.skilldef_invisible_cloak['name_skill'], self.charactercreation.characters)

                    else:
                        self.duel_action_choices(player)
                        back_to_action_choices = True
                        return back_to_action_choices
                    


                if self.charactercreation.characters[player]['class'] == 'Necromante':

                    print(f"{self.skilldef_bone_shield['id_skill']} - {self.skilldef_bone_shield['name_skill']}\n{self.skilldef_bone_shield['info_skill']['skill_desc']}")

                    final_choice_confirm = input("Deseja realizar esta defesa? (S/N)").upper()

                    if final_choice_confirm == 'S':
                        self.skilldef.skill_defense(player, self.skilldef_bone_shield['name_skill'], self.charactercreation.characters)

                    else:
                        self.duel_action_choices(player)
                        back_to_action_choices = True
                        return back_to_action_choices
                    


                if self.charactercreation.characters[player]['class'] == 'Bruxa':

                    print(f"{self.skilldef_bad_and_good_luck['id_skill']} - {self.skilldef_bad_and_good_luck['name_skill']}\n{self.skilldef_bad_and_good_luck['info_skill']['skill_desc']}")

                    final_choice_confirm = input("Deseja realizar esta defesa? (S/N)").upper()

                    if final_choice_confirm == 'S':
                        self.skilldef.skill_defense(player, self.skilldef_bad_and_good_luck['name_skill'], self.charactercreation.characters)

                    else:
                        self.duel_action_choices(player)
                        back_to_action_choices = True
                        return back_to_action_choices
                    


            else:
                print(f"Você não possui vigor o suficiente ({self.charactercreation.characters[player]['stamina']}) para realizar esta ação (custo: {self.skillsplatk.skill_spl_attack_cost}).\nPor gentileza, selecione outra ação ou utilize seu turno para descansar.")
                self.duel_action_choices(player)
                back_to_action_choices = True
                return back_to_action_choices
            


        if final_choice == 'Evasão':
            pass



        if final_choice == 'Cura':
            pass



        if final_choice == 'Descanso':
            pass

        

duelaction = DuelAction()

if __name__ == '__main__':
    duelactionchoice = duelaction.duel_action_choices('gab')
    #print(duelactionchoice)
    duelactionmove = duelaction.duel_action_move('gab', 'gui', duelactionchoice)
    #print(duelactionmove)