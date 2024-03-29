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
        pass



skillnat = SkillNaturalAbility()



if __name__ == '__main__':
    pass