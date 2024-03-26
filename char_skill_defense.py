import random

class SkillDefense:

    def __init__(self):
        self.skill_def_cost = 2
        self.skill_def_cooldown = 1
        self.skill_def_cooldown_on = False
        self.skill_next_id = 0
        self.skills_def = []
    
    def skill_def_creation(self, skill_class, skill_name, skill_details):
        skill_id = self.skill_next_id
        skill_info = dict(zip(['skill_desc', 'skill_effect_desc', 'skill_effect', 'skill_roll'], skill_details))
        new_skill = {'id_skill': skill_id, 'class_skill': skill_class, 'name_skill': skill_name, 'info_skill': skill_info}
        self.skills_def.append(new_skill)
        self.skill_next_id += 1
        return new_skill
    
    def skill_defense_effect(self):
        pass

    def skill_defense(self, defenser, skill_name):
        skill_roll = skill_name['info_skill']['skill_roll']
        skill_value = defenser['att_groups']['DEF']
        skill_armor = defenser['current_armor']
        skill_defense = skill_roll + skill_value + skill_armor
        skill_effect = skill_name['info_skill']['skill_effect']
        print(f"Dado: {skill_roll} + Atributo def: {skill_value} + {skill_armor} = Defesa total: {skill_defense}")
        return skill_roll, skill_value, skill_armor, skill_defense, skill_effect

skilldef = SkillDefense()

if __name__ == '__main__':
    pass