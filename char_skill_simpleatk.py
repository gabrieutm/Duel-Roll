import random
#from char_skill_effect import charskilleffect

class SkillSimpleAttack:

    def __init__(self):
        self.skill_spl_attack_cost = 3
        self.skill_spl_attack_cooldown = 0
        self.skill_spl_attack_cooldown_on = False
        self.skill_next_id = 0
        self.skills_spl_attack = []



    def skill_spl_attack_creation(self, skill_class, skill_name, skill_details):
        skill_id = self.skill_next_id
        
        skill_info = dict(zip(['skill_desc', 'skill_effect_desc', 'skill_effect', 'skill_roll'], skill_details))
        
        new_skill = {'id_skill': skill_id, 'class_skill': skill_class, 'name_skill': skill_name, 
        'info_skill': skill_info}
        
        self.skills_spl_attack.append(new_skill)
        self.skill_next_id += 1
        return new_skill



    def skill_spl_attack_effect(self):
        pass



    def skill_spl_attack_hit(self, attacker, enemy, characters, menu):

        class_skills = []
        
        for skills in skillsplatk.skills_spl_attack:
        
            for skill_values in skills.values():
                
                if skill_values == attacker['class']:

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
                        skill_value = attacker['att_groups']['ATK']
                        skill_damage = skill_roll + skill_value
                        skill_effect = chosen_skill['info_skill']['skill_effect']
                        
                        print(f"Dado: {skill_roll} + Atributo atk: {skill_value} = Dano total: {skill_damage}")

                        remaining_hp = characters[enemy]['current_hp'] - skill_damage
                        characters[enemy]['current_hp'] = remaining_hp
                        print(f"Vida restante de {enemy}: {max(remaining_hp, 0)}")

                        remaining_stamina = max(0, characters[attacker]['stamina'] - self.skill_spl_attack_cost)
                        characters[attacker]['stamina'] = remaining_stamina
                        print(f"Vigor restante de {attacker}: {remaining_stamina}")

                        skill_return = (skill_roll, skill_value, skill_damage, skill_effect, remaining_hp, remaining_stamina)
                        
                        return skill_return
                    
                    else:
                        continue
                
                else:
                    print("Entrada inválida. Por favor, insira um número da lista.")
                    continue
            
            except:
                print("Entrada inválida. Por favor, insira um número da lista.")
                continue



skillsplatk = SkillSimpleAttack()



skillsplatk_ethereal_burst = skillsplatk.skill_spl_attack_creation('Mago', 'Rajada Etérea', ('O mago ergue as mãos, concentrando energia, e dispara uma rajada etérea em direção ao alvo, causando danos mágicos instáveis.', 'Se o inimigo tentar atacar no turno seguinte, ele recebe 1-4 de dano.', None, random.randint(1, 4)))



skillsplatk_wild_charge = skillsplatk.skill_spl_attack_creation('Bárbaro', 'Investida Selvagem', ('O bárbaro avança furiosamente sobre seu adversário, desferindo um impacto brutal.', 'Se o dado de dano rolar 2 ou menos na primeira vez, o dado é rolado de novo, usando o resultado mais alto.', None, random.randint(1, 4)))



skillsplatk_shadow_arrow = skillsplatk.skill_spl_attack_creation('Assassino', 'Flecha das Sombras', ('O assassino furtivamente lança uma flecha sileciosa das sombras que perfura o alvo dolorosamente.', 'Se o dado de dano rolar o número máximo, ganha 1-4 para a próxima habilidade utilizada.', None, random.randint(1, 4)))



skillsplatk_skeleton = skillsplatk.skill_spl_attack_creation('Necromante', 'Esqueleto', ('O necromante ergue uma alma esquelética que avança para atacar o inimigo.', 'Se o dado de dano rolar o número máximo, ao final do próximo turno do oponente, o esqueleto atacará de novo por conta própria, causando 1-4 de dano.', None, random.randint(1, 4)))



skillsplatk_excruciating_gaze = skillsplatk.skill_spl_attack_creation('Bruxa', 'Olhar Torturante', ('A bruxa encara o inimigo, alcançando sua alma para causar uma dor intolerável, deixando o alvo vulnerável a ataques.', 'Se o dado de dano rolar o número máximo, ele é rolado novamente e seu novo valor é adicionado junto.', None, random.randint(1, 4)))



if __name__ == "__main__":
    print(skillsplatk_excruciating_gaze)