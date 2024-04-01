import random

class SkillNaturalAbility:

    def __init__(self):
        self.skill_nat_cooldown = 3
        self.skill_nat_cooldown_on = False
        self.skill_next_id = 0
        self.skills_nat = []
    
    

    def skill_nat_creation(self, skill_class, skill_name, skill_att_groups, skill_details):
        skill_id = self.skill_next_id

        skill_info = dict(zip(['skill_desc', 'skill_effect_desc', 'skill_effect', 'skill_roll'], skill_details))

        new_skill = {'id_skill': skill_id, 'class_skill': skill_class, 'name_skill': skill_name, 'att_groups_skill': skill_att_groups, 'info_skill': skill_info}

        self.skills_nat.append(new_skill)
        self.skill_next_id += 1
        return new_skill
    


    def skill_nat_effect(self):
        pass



    def skill_nat(self, player, enemy, characters, menu):

        for skills in skillnat.skills_nat:
        
            for skill_values in skills.values():
                
                if skill_values == characters[player]['class']:

                    while True:

                        print(f"{skills['name_skill']}\n{skills['info_skill']['skill_desc']}")

                        chosen_skill_confirm = input(f"Tem certeza que deseja usar esta habilidade? (S/N) ").upper()

                        if chosen_skill_confirm == 'S':
                            print('ok')
                            #criar o efeito das nat e então colocar elas num dicionário filtrando por nome
                        
                        else:

                            menu(player, enemy)
                            break

skillnat = SkillNaturalAbility()



skillnat_enchantment = skillnat.skill_nat_creation('Mago', 'Encantamento', ['ATK'], ('O mago utiliza seu conhecimento para ampliar seus poderes, se conseguir recitar as palavras corretas.', 'Por um turno, se o dado cair entre 1-3, perde um ponto no valor de todos os atributos. Caso contrário, escolhe um atributo para ganhar 1-3 pontos.', None, random.randint(1, 6)))



skillnat_rage = skillnat.skill_nat_creation('Bárbaro', 'Fúria', None, ('O bárbaro irrompe em cólera, aumentando sua ferocidade, enquanto fica vulnerável a ataques.', 'Ganha vantagem no próximo ataque, mas o oponente ganha vantagam contra você também.', None, 0))



skillnat_impulsion = skillnat.skill_nat_creation('Assassino', 'Impulsão', ['ATK','DEF','HLN'], ('O assassino manipula o combate a seu favor, enquanto o inimigo prepara sua defesa.', 'Rouba um ponto de cada atributo do oponente para si, mas ele ganha +1 de armadura.', None, 0))



skillnat_mortal_force = skillnat.skill_nat_creation('Necromante', 'Força Mortal', ['ATK','DEF','HLN'], ('O necromante abre mão de sua própria vida para ampliar seus poderes corrompidos.', 'Sacrifica 1-6 pontos de vida para utilizar o mesmo valor na próxima habilidade.', None, random.randint(1, 6)))



skillnat_hex = skillnat.skill_nat_creation('Bruxa', 'Maldição', ['ATK','DEF','HLN'], ('A bruxa lança sobre o oponente uma danação que cai sobre o inimigo, a custo da sua própria fortuna.', 'Impede que um tipo de ação seja feita no duelo, tanto para o oponente quanto para si.'))



if __name__ == '__main__':
    print(skillnat_hex)