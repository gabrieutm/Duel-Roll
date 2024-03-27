import random

class SkillDefense:

    def __init__(self):
        self.skill_def_cost = 1
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
        skill_defense_total = skill_roll + skill_value + skill_armor
        skill_effect = skill_name['info_skill']['skill_effect']
        defenser['current_armor'] = skill_defense_total
        print(f"Dado: {skill_roll} + Atributo def: {skill_value} + {skill_armor} = Defesa total: {skill_defense_total}")
        return skill_roll, skill_value, skill_armor, skill_defense_total, skill_effect

skilldef = SkillDefense()

skilldef_magic_shield = skilldef.skill_def_creation('Mago', 'Escudo Mágico', ('O mago conjura uma barreira de energia arcana que repele ataques físicos e mágicos, protegendo-o dos perigos iminentes.', 'Até o final do próximo turno do oponente, você ganha 1-4+DEF de armadura e, caso o oponente conseguir acertar um ataque, se o dano for maior ou igual a sua vida atual, ele é reduzido pela metade.', None, random.randint(1, 4)))

skilldef_iron_skin = skilldef.skill_def_creation('Bárbaro', 'Pele de Ferro', ('O bárbaro enrijece seus musculos, fortalecendo seu corpo com uma resistência sobre-humana, tornando o quase impenetrável aos ataques dos inimigos.', 'Até o final do próximo turno do oponente, você ganha 1-4+DEF de armadura e, caso o oponente conseguir acertar um ataque, ele é reduzido pelo total da sua armadura atual.', None, random.randint(1, 4)))

skilldef_invisible_cloak = skilldef.skill_def_creation('Assassino', 'Capa da Invisibilidade', ('O assassino se envolve em seu manto, desaparecendo, tornando-se difícil de atingir.', 'Até o final do próximo turno do oponente, você ganha 1-4+DEF de armadura e o oponente tem desvantagem na rolagem de acerto.', None, random.randint(1, 4)))

skilldef_bone_shield = skilldef.skill_def_creation('Necromante', 'Escudo de Ossos', ('O necromante manipula os restos mortais calcificados ao seu redor e envolve sua armadura em ossos quase indestrutíveis.', 'Até o final do próximo turno do oponente, você ganha 1-4+DEF de armadura e, caso o oponente consiga acertar um ataque, estilhaços de ossos voam na direçam dele, causando 1-4 de dano.', None, random.randint(1, 4)))

skilldef_bone_shield = skilldef.skill_def_creation('Necromante', 'Escudo de Ossos', ('O necromante manipula os restos mortais calcificados ao seu redor e envolve sua armadura em ossos quase indestrutíveis.', 'Até o final do próximo turno do oponente, você ganha 1-4+DEF de armadura e, caso o oponente consiga acertar um ataque, estilhaços de ossos voam na direçam dele, causando 1-4 de dano.', None, random.randint(1, 4)))

skilldef_bad_and_good_luck = skilldef.skill_def_creation('Bruxa', 'Sorte e Azar', ('A bruxa canaliza seu poder para alterar os destinos e evitar ser atacada.', 'Até o final do próximo turno do oponente, ele tem ataque reduzido igual a seu atributo de defesa e você ganha 1-4+DEF de armadura.', None, random.randint(1, 4)))

if __name__ == '__main__':
    print(skilldef_bone_shield)