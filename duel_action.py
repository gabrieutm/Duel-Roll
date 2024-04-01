class DuelAction:

    def __init__(self):
        """
        from char_skill_evasion import skilleva
        self.skilleva = skilleva
        from char_skill_rest import rest
        self.rest = rest
"""
        from char_skill_forceatk import skillfrcatk,skillfrcatk_fireball, skillfrcatk_warhammer, skillfrcatk_poisoned_dagger, skillfrcatk_reaper_spirit, skillfrcatk_death_ray

        self.skillfrcatk = skillfrcatk
        self.skillfrcatk_fireball = skillfrcatk_fireball
        self.skillfrcatk_warhammer = skillfrcatk_warhammer
        self.skillfrcatk_poisoned_dagger = skillfrcatk_poisoned_dagger
        self.skillfrcatk_reaper_spirit = skillfrcatk_reaper_spirit
        self.skillfrcatk_death_ray = skillfrcatk_death_ray

        
        
        from char_skill_healing import skillhln, skillhln_arcane_regeneration, skillhln_new_scar, skillhln_transfusion, skillhln_hematurgic, skillhln_cauldron_of_souls
        
        self.skillhln = skillhln
        self.skillhln_arcane_regeneration = skillhln_arcane_regeneration
        self.skillhln_new_scar = skillhln_new_scar
        self.skillhln_transfusion = skillhln_transfusion
        self.skillhln_hematurgic = skillhln_hematurgic
        self.skillhln_cauldron_of_souls = skillhln_cauldron_of_souls



        from char_skill_special import skillspc, skillspc_genesis_overload, skillspc_berserker_extermination, skillspc_marked_to_death, skillspc_the_devils_fear, skillspc_voodoo_doll

        self.skillspc = skillspc
        self.skillspc_genesis_overload = skillspc_genesis_overload
        self.skillspc_berserker_extermination = skillspc_berserker_extermination
        self.skillspc_marked_to_death = skillspc_marked_to_death
        self.skillspc_the_devils_fear = skillspc_the_devils_fear
        self.skillspc_voodoo_doll = skillspc_voodoo_doll

        
        
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



    def duel_action_choices(self, player, enemy, menu):

        self.action_groups = {1: {'Atacar': {1: 'Ataque Simples', 2: 'Ataque Poderoso', 3: 'Ataque Especial'}}, 2: {'Defender': {1: 'Defesa', 2: 'Evasão'}}, 3: {'Curar': {1: 'Cura', 2: 'Descanso'}}}
        
        while True:

            print("Opções de ações: ")
            
            for key, value in self.action_groups.items():
                print(f"{key} - {list(value.keys())[0]}")

            choice = int(input("Escolha digitando o respectivo número da ação (ou 0 a qualquer momento para voltar ao menu anterior): "))

            if choice == 0:
                menu(player)

            elif choice in self.action_groups.keys():

                if choice == 1:

                    while True:
                        
                        print("Opções de ataque: ")
                        
                        for key, value in self.action_groups[1]['Atacar'].items():
                            print(f"{key} - {value}")
                        
                        final_choice = int(input("Escolha digitando o respectivo número do ataque: "))
                        
                        if final_choice == 0:
                            break
                        
                        elif final_choice in self.action_groups[1]['Atacar'].keys():
                            final_choice = self.action_groups[1]['Atacar'][final_choice]
                            


                            if final_choice == 'Ataque Simples':

                                if self.duel_action_stamina_check(player, self.skillsplatk.skill_spl_attack_cost) == True:

                                    print("Opções de Ataque Simples: ")
                                    
                                    return self.skillsplatk.skill_spl_attack_hit(player, enemy, self.charactercreation.characters, menu)

                                else:
                                    print(f"Você não possui vigor o suficiente ({self.charactercreation.characters[player]['stamina']}) para realizar esta ação (custo: {self.skillsplatk.skill_spl_attack_cost}).\nPor gentileza, selecione outra ação ou utilize seu turno para descansar.")

                                    return self.duel_action_choices(player, enemy)
                            


                            elif final_choice == 'Ataque Poderoso':
            
                                if self.duel_action_stamina_check(player, self.skillfrcatk.skill_frc_attack_cost) == True:

                                    print("Opções de Ataque Poderoso: ")
                                    
                                    return self.skillfrcatk.skill_frc_attack_hit(player, enemy, self.charactercreation.characters, menu)

                                else:
                                    print(f"Você não possui vigor o suficiente ({self.charactercreation.characters[player]['stamina']}) para realizar esta ação (custo: {self.skillfrcatk.skill_frc_attack_cost}).\nPor gentileza, selecione outra ação ou utilize seu turno para descansar.")

                                    return self.duel_action_choices(player, enemy)
                                


                            elif final_choice == 'Ataque Especial':
            
                                if self.duel_action_stamina_check(player, self.skillspc.skill_spc_cost) == True:

                                    print("Opções de Ataque Especial: ")
                                    
                                    return self.skillspc.skill_spc(player, enemy, self.charactercreation.characters, menu)

                                else:
                                    print(f"Você não possui vigor o suficiente ({self.charactercreation.characters[player]['stamina']}) para realizar esta ação (custo: {self.skillspc.skill_spc_cost}).\nPor gentileza, selecione outra ação ou utilize seu turno para descansar.")

                                    return self.duel_action_choices(player, enemy)
                                

                        
                        else:
                            print("Entrada inválida. Por favor, insira um número da lista.")
                            continue
                    
                    break
                
                if choice == 2:
                    
                    while True:
                        
                        print("Opções de defesa: ")
                        
                        for key, value in self.action_groups[2]['Defender'].items():
                            print(f"{key} - {value}")
                        
                        final_choice = int(input("Escolha digitando o respectivo número da defesa: "))
                        
                        if final_choice == 0:
                            break
                        
                        elif final_choice in self.action_groups[2]['Defender'].keys():
                            final_choice = self.action_groups[2]['Defender'][final_choice]
                            
                            

                            if final_choice == 'Defesa':

                                if self.duel_action_stamina_check(player, self.skilldef.skill_def_cost) == True:

                                    print("Opções de Defesa: ")

                                    return self.skilldef.skill_defense(player, self.charactercreation.characters, menu)

                                else:
                                    print(f"Você não possui vigor o suficiente ({self.charactercreation.characters[player]['stamina']}) para realizar esta ação (custo: {self.skilldef.skill_def_cost}).\nPor gentileza, selecione outra ação ou utilize seu turno para descansar.")

                                    return self.duel_action_choices(player, enemy)
                                


                            elif final_choice == 'Evasão':
                                pass #fazer
                        
                        else:
                            print("Entrada inválida. Por favor, insira um número da lista.")
                            continue
                    
                    break

                if choice == 3:
                    
                    while True:
                        
                        print("Opções de cura: ")
                        
                        for key, value in self.action_groups[3]['Curar'].items():
                            print(f"{key} - {value}")
                        
                        final_choice = int(input("Escolha digitando o respectivo número da cura: "))
                        
                        if final_choice == 0:
                            break
                        
                        elif final_choice in self.action_groups[3]['Curar'].keys():
                            self.final_choice = self.action_groups[3]['Curar'][final_choice]



                            if final_choice == 'Cura':
            
                                if self.duel_action_stamina_check(player, self.skillhln.skill_healing_cost) == True:

                                    print("Opções de Cura: ")

                                    return self.skillhln.skill_healing(player, self.charactercreation.characters, menu)

                                else:
                                    print(f"Você não possui vigor o suficiente ({self.charactercreation.characters[player]['stamina']}) para realizar esta ação (custo: {self.skillhln.skill_healing_cost}).\nPor gentileza, selecione outra ação ou utilize seu turno para descansar.")

                                    return self.duel_action_choices(player, enemy)
                                


                            elif final_choice == 'Descanso':
                                    pass #fazer
                        


                        else:
                            print("Entrada inválida. Por favor, insira um número da lista.")
                            continue
                    
                    break

            else:
                print("Entrada inválida. Por favor, insira um número da lista.")
                continue



duelaction = DuelAction()



if __name__ == '__main__':
    duelactionchoice = duelaction.duel_action_choices('gab')
    #print(duelactionchoice)
    duelactionmove = duelaction.duel_action_move('gab', 'gui', duelactionchoice)
    #print(duelactionmove)