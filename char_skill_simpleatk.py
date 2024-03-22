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
        skill_info = dict(zip(['skill_desc', 'skill_roll', 'skill_effect'], skill_details))
        new_skill = {'id_skill': skill_id, 'class_skill': skill_class, 'name_skill': skill_name, 'info_skill': skill_info}
        self.skills_spl_attack.append(new_skill)
        self.skill_next_id += 1
        return new_skill

    def skill_spl_attack_effect(self):
        pass
    
    def skill_spl_attack_hit(self, skill_name, attacker, atk_value, deffender):
        skill_roll = skill_name['info_skill']['skill_roll']
        skill_damage = skill_roll + atk_value
        skill_result = enemy['current_hp'] - skill_damage
        print(f"\nDado: {skill_roll}.\nVocê causou {skill_damage} de dano a {enemy}.")
        return skill_result

skillsimpleattack = SkillSimpleAttack()

skill_spl_atk_ethereal_ray = skillsimpleattack.skill_spl_attack_creation('Mago', 'Raio Etéreo', ('O mago ergue as mãos, concentrando energia, e dispara um raio etéreo em direção ao alvo, causando danos mágicos instáveis. Se o inimigo tentar atacar no turno seguinte, ele recebe 1-4 de dano.', random.randint(1, 4), None))

if __name__ == "__main__":
    print(skill_spl_atk_ethereal_ray['info_skill']['skill_roll'])