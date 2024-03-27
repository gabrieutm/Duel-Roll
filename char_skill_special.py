import random
#from char_skill_effect import charskilleffect

class SkillSpecial:

    def __init__(self):
        self.skill_spc_cost = 5
        self.skill_spc_cooldown = 3
        self.skill_spc_cooldown_on = False
        self.skill_next_id = 0
        self.skills_spc = []

    def skill_spc_creation(self, skill_class, skill_name, skill_details):
        skill_id = self.skill_next_id
        skill_info = dict(zip(['skill_desc', 'skill_effect_desc', 'skill_effect', 'skill_roll'], skill_details))
        new_skill = {'id_skill': skill_id, 'class_skill': skill_class, 'name_skill': skill_name, 'info_skill': skill_info}
        self.skills_spc.append(new_skill)
        self.skill_next_id += 1
        return new_skill

    def skill_spc_effect(self):
        pass
    
    def skill_spc_hit(self, attacker, skill_name):
        skill_roll = skill_name['info_skill']['skill_roll']
        skill_value = attacker['att_groups']['ATK']
        skill_damage = skill_roll + skill_value
        skill_effect = skill_name['info_skill']['skill_effect']
        print(f"Dado: {skill_roll} + Atributo atk: {skill_value} = Dano total: {skill_damage}")
        return skill_roll, skill_value, skill_damage, skill_effect

skillsplatk = SkillSpecial()

if __name__ == '__main__':
    pass