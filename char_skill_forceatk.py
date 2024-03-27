import random
#from char_skill_effect import charskilleffect

class SkillForceAttack:

    def __init__(self):
        self.skill_frc_attack_cost = 4
        self.skill_frc_attack_cooldown = 1
        self.skill_frc_attack_cooldown_on = False
        self.skill_next_id = 0
        self.skills_frc_attack = []

    def skill_frc_attack_creation(self, skill_class, skill_name, skill_details):
        skill_id = self.skill_next_id
        skill_info = dict(zip(['skill_desc', 'skill_effect_desc', 'skill_effect', 'skill_roll'], skill_details))
        new_skill = {'id_skill': skill_id, 'class_skill': skill_class, 'name_skill': skill_name, 'info_skill': skill_info}
        self.skills_frc_attack.append(new_skill)
        self.skill_next_id += 1
        return new_skill

    def skill_frc_attack_effect(self):
        pass
    
    def skill_spl_attack_hit(self, attacker, skill_name):
        skill_roll = skill_name['info_skill']['skill_roll']
        skill_value = attacker['att_groups']['ATK']
        skill_damage = skill_roll + skill_value
        skill_effect = skill_name['info_skill']['skill_effect']
        print(f"Dado: {skill_roll} + Atributo atk: {skill_value} = Dano total: {skill_damage}")
        return skill_roll, skill_value, skill_damage, skill_effect

skillsplatk = SkillForceAttack()

if __name__ == '__main__':
    pass