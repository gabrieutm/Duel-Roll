import random
#from char_skill_effect import charskilleffect

class SkillHealing:

    def __init__(self):
        self.skill_healing_cost = 3
        self.skill_healing_cooldown = 1
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
    
    def skill_healing(self, healer, skill_name):
        skill_roll = skill_name['info_skill']['skill_roll']
        skill_value = healer['att_groups']['HLN']
        skill_heal = skill_roll + skill_value
        skill_effect = skill_name['info_skill']['skill_effect']
        print(f"Dado: {skill_roll} + Atributo hln: {skill_value} = Cura total: {skill_heal}")
        return skill_roll, skill_value, skill_heal, skill_effect

skillsplatk = SkillHealing()

if __name__ == '__main__':
    pass