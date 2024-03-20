class CharPoint:

    def __init__(self):

        from char_race import race_human, race_elf, race_dwarf, race_orc, race_animana
        self.race_human = race_human
        self.race_elf = race_elf
        self.race_dwarf = race_dwarf
        self.race_orc = race_orc
        self.race_animana = race_animana

        from char_attribute import attributes_groups
        self.attributes_groups = {key: 0 for key in attributes_groups}

        self.attributes_groups_human = self.attributes_groups.copy()
        self.attributes_groups_elf = self.attributes_groups.copy()
        self.attributes_groups_dwarf = self.attributes_groups.copy()
        self.attributes_groups_orc = self.attributes_groups.copy()
        self.attributes_groups_animana = self.attributes_groups.copy()
    
    def point_distribution_human(self):
        points_extra_human = self.race_human['initial_stats_race']['race_initial_points']
        for attribute in self.attributes_groups_human.keys():
            self.attributes_groups_human[attribute] = 1
            points_extra_human -= 1
            if points_extra_human == 0:
                break
        
        print(f"Você é um(a) humano(a) e recebe 3 pontos extras iniciais que são igualmente dividos entre os atributos.")

        return self.attributes_groups_human
    
    def point_distribution_elf(self):
        points_extra_elf = self.race_elf['initial_stats_race']['race_initial_points']
        print("Você é um(a) elfo(a) e recebe 3 pontos extras iniciais para distribuir, de forma que 2 pontos são adicionados a um atributo e 1 ponto restante é adicionado a outro atributo diferente.")
        
        while points_extra_elf > 1:
            att_2_points = input("Em qual atributo deseja colocar 2 pontos (ATK, DEF, HLN)? ").upper()
            if att_2_points in self.attributes_groups_elf.keys():
                self.attributes_groups_elf[att_2_points] += 2
                points_extra_elf -= 2
            else:
                print("Atributo inválido.")
        
        while points_extra_elf > 0:
            att_1_point = input("Em qual atributo deseja colocar 1 ponto (ATK, DEF, HLN, diferente do anterior)? ").upper()
            if att_1_point in self.attributes_groups_elf.keys() and att_1_point != att_2_points:
                self.attributes_groups_elf[att_1_point] += 1
                points_extra_elf = 0
            else:
                print("Atributo inválido ou igual ao primeiro.")
        
        print(f"Você distribuiu 2 pontos em {att_2_points} e 1 ponto em {att_1_point} para os atributos.")
        
        return self.attributes_groups_elf

    def point_distribution_dwarf(self):
        points_extra_dwarf = self.race_dwarf['initial_stats_race']['race_initial_points']
        print("Você é um(a) anão(a) e recebe 3 pontos extras iniciais para atribuir um único atributo da sua escolha.")

        while points_extra_dwarf > 0:
            att_3_points = input("Em qual atributo deseja colocar todos os 3 pontos (ATK, DEF, HLN)? ").upper()
            if att_3_points in self.attributes_groups_dwarf.keys():
                self.attributes_groups_dwarf[att_3_points] += 3
                points_extra_dwarf = 0
            else:
                print("Atributo inválido.")
        
        return self.attributes_groups_dwarf

    def point_distribution_orc(self):
        points_extra_orc = self.race_orc['initial_stats_race']['race_initial_points']
        print("Você é um(a) orc e recebe somente 1 ponto extra inicial para atribuir a um único atributo da sua escolha.")

        while points_extra_orc > 0:
            att_1_point = input("Em qual atributo deseja colocar 1 ponto (ATK, DEF, HLN)? ").upper()
            if att_1_point in self.attributes_groups_orc.keys():
                self.attributes_groups_orc[att_1_point] += 1
                points_extra_orc = 0
            else:
                print("Atributo inválido.")
        
        return self.attributes_groups_orc

    def point_distribution_animana(self):
        points_extra_animana = self.race_animana['initial_stats_race']['race_initial_points']
        print("Você é um(a) animana e recebe 4 pontos extras iniciais para distribuir, de forma que 3 pontos são adicionados a um atributo e 1 ponto restante é adicionado a outro atributo diferente.")
        
        while points_extra_animana > 2:
            att_3_points = input("Em qual atributo deseja colocar 3 pontos (ATK, DEF, HLN)? ").upper()
            if att_3_points in self.attributes_groups_animana.keys():
                self.attributes_groups_animana[att_3_points] += 3
                points_extra_animana -= 3
            else:
                print("Atributo inválido.")
        
        while points_extra_animana > 0:
            att_1_point = input("Em qual atributo deseja colocar 1 ponto (ATK, DEF, HLN, diferente do anterior)? ").upper()
            if att_1_point in self.attributes_groups_animana.keys() and att_1_point != att_3_points:
                self.attributes_groups_animana[att_1_point] += 1
                points_extra_animana = 0
            else:
                print("Atributo inválido ou igual ao primeiro.")
        
        print(f"Você distribuiu 3 pontos em {att_3_points} e 1 ponto em {att_1_point} para os atributos.")
        
        return self.attributes_groups_animana

point = CharPoint()

points_distribution = {0: point.point_distribution_human,
                       1: point.point_distribution_elf,
                       2: point.point_distribution_dwarf,
                       3: point.point_distribution_orc,
                       4: point.point_distribution_animana}

if __name__ == "__main__":
    point.point_distribution_human()
    point.point_distribution_elf()
    point.point_distribution_dwarf()
    point.point_distribution_orc()
    point.point_distribution_animana()