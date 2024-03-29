import random
#from char_skill_effect import charskilleffect

class SkillHealing:

    def __init__(self):
        self.skill_healing_cost = 2
        self.skill_healing_cooldown = 2
        self.skill_healing_cooldown_on = False
        self.skill_next_id = 0
        self.skills_healing = []



    def skill_healing_creation(self, skill_class, skill_name, skill_details):
        skill_id = self.skill_next_id

        skill_info = dict(zip(['skill_desc', 'skill_effect_desc', 'skill_effect', 'skill_roll'], skill_details))
        
        new_skill = {'id_skill': skill_id, 'class_skill': skill_class, 'name_skill': skill_name, 'info_skill': skill_info}
        
        self.skills_healing.append(new_skill)
        self.skill_next_id += 1
        return new_skill



    def skill_healing_effect(self):
        pass
    


    def skill_healing(self, healer, characters, menu):
        class_skills = []
        
        for skills in skillhln.skills_healing:
        
            for skill_values in skills.values():
                
                if skill_values == healer['class']:

                    class_skills.append(skills)
        
        class_skills = {index: skill for index, skill in enumerate(class_skills)}

        while True:

            for key, skill in class_skills.items():
                print(f"{key} - {skill['name_skill']}\n{skill['info_skill']['skill_desc']}")
                
            choose_skill = input("Digite o respectivo número da habilidade que deseja utilizar: (ou digite 'voltar')").lower()
            
            try:

                if choose_skill == 'voltar':

                    menu()
                    break

                elif int(choose_skill) in class_skills.keys():

                    chosen_skill = class_skills[int(choose_skill)]

                    chosen_skill_confirm = input(f"Tem certeza que deseja usar a habilidade {chosen_skill['name_skill']}? (S/N) ").upper()
            
                    if chosen_skill_confirm == 'S':
                            
                        skill_roll = chosen_skill['info_skill']['skill_roll']
                        skill_value = healer['att_groups']['HLN']
                        skill_hp = healer['current_hp']
                        skill_heal_total = skill_roll + skill_value + skill_hp
                        skill_effect = chosen_skill['info_skill']['skill_effect']
                        healer['current_hp'] = min(skill_heal_total, healer['max_hp'])
                        print(f"Dado: {skill_roll} + Atributo hln: {skill_value} + HP: {skill_hp} = Cura total: {skill_heal_total}")
                        remaining_stamina = max(0, characters[healer]['stamina'] - skillhln.skill_healing_cost)
                        characters[healer]['stamina'] = remaining_stamina
                        print(f"Vigor restante de {healer}: {remaining_stamina}")

                        skill_result = (skill_roll, skill_value, skill_hp, skill_heal_total, skill_effect, remaining_stamina)

                        break
                    
                    else:
                        continue
                
                else:
                    print("Entrada inválida. Por favor, insira um número da lista.")
                    continue
            
            except:
                print("Entrada inválida. Por favor, insira um número da lista.")
                continue



skillhln = SkillHealing()



skillhln_arcane_regeneration = skillhln.skill_healing_creation('Mago', 'Regeneração Arcana', ('O mago canaliza a energia arcana para restaurar rapidamente sua vitalidade, fortalecendo-se com a essência mágica que o envolve.', 'Ao ser utilizada, escolhe um atributo para que seu valor seja duplicado até o final do seu próximo turno.', None, random.randint(1, 6)))



skillhln_new_scar = skillhln.skill_healing_creation('Bárbaro', 'Nova Cicatriz', ('O bárbaro, em um momento de fúria e resistência, abraça a dor e transforma suas feridas em força renovada, emergindo com uma nova determinação e poder.', 'Até o final do próximo turno do inimigo, ele tem desvantagem para atacar você.', None, random.randint(1, 6)))



skillhln_transfusion = skillhln.skill_healing_creation('Assassino', 'Transfusão', ('O assassino utiliza um líquido sinistro, infundido com o sangue de seus adversários mais poderosos, para uma transfusão misteriosa que o deixa mais resistente.', 'Por um turno, recebe somente metade do dano do próximo ataque do adversário.', None, random.randint(1, 6)))



skillhln_hematurgic = skillhln.skill_healing_creation('Necromante', 'Hematurgia', ('O necromante controla o próprio sangue para fechar suas feridas e voltar com mais essência vital.', 'Ganha 1-6 pontos de vida temporários.', None, random.randint(1, 6)))



skillhln_cauldron_of_souls = skillhln.skill_healing_creation('Bruxa', 'Caldeirão de Almas', ('A bruxa invoca seu caldeirão e absorve a essência de uma alma aprisionada nele para se curar e ficar mais monstruosa.', 'Se a cura dessa habilidade atingir a vida máxima, pode realizar mais uma ação no mesmo turno.', None, random.randint(1, 6)))



if __name__ == '__main__':
    print(skillhln_cauldron_of_souls)