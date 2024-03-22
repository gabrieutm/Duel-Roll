class SkillDef:

    def __init__(self):
        
        import random
        self.random = random

        self.skill_def_cost = 2
        self.skill_def_cooldown = 0
    
    def skill_def(self, player, skill, current_stamina):
        if current_stamina >= self.skill_def_cost:
            current_stamina =- self.skill_def_cost
            print(f"{player} utilizou a habilidade de defesa {skill}. Vigor atual: {current_stamina}.")
        else:
            print(f"Você não possui vigor o suficiente para usar esta habilidade. Por favor, escolha outra ação.")
    
    def skill_def_class_mage(self, def_mod):
        #ESCUDO MÁGICO: conjura um escudo de magia arcana que fortifica a armadura por um turno
        skill_roll = self.random.randint(1, 6)
        skill_value = skill_roll + def_mod
        print(f"A armadura foi fortificada em {skill_value}.")