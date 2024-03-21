class Character:

    def __init__(self):

        import char_armor
        self.char_armor = char_armor

        import char_attribute
        self.char_attribute = char_attribute

        import char_class
        self.char_class = char_class

        import char_hp
        self.char_hp = char_hp

        import char_point
        self.char_point = char_point

        import char_race
        self.char_race = char_race

        import char_stamina
        self.char_stamina = char_stamina

    def character_selection(self):
        self.char_id_race = self.char_race.race.race_selection()
        self.char_race_name = self.char_race.races_id_name[self.char_id_race]

        self.char_id_class = self.char_class.classs.class_selection()
        self.char_class_name = self.char_class.classes_id_name[self.char_id_class]

        while True:
            self.char_name = input("Digite o nome do seu personagem: ").upper()
            if not self.char_name.isalpha():
                print("O nome não pode conter números ou caracteres inválidos. Tente novamente.")
            elif len(self.char_name) > 35:
                print("O nome do personagem deve ter no máximo 35 caracteres. Tente novamente.")
            else:
                break
    
    def character_points(self):
        char_point_distribution = self.char_point.points_distribution[self.char_id_race]()

        id_att = self.char_attribute.attribute.attributes[self.char_id_class]
        
        for group, mod_value in char_point_distribution.items():
            id_att[group]['att_mod'], id_att[group]['att_value'] = mod_value, mod_value

        char_att = self.char_attribute.attribute.att_roll()
        char_att_rolls = char_att.copy()

        for group, mod_value in char_point_distribution.items():
            char_att[group] += mod_value

        for group, total_value in char_att.items():
            id_att[group]['att_value'] = total_value
        
        char_hp_roll = self.char_hp.hp.hp_roll(self.char_id_race)
        char_max_hp = char_hp_roll[2] +  + char_att['HLN']

        char_armor_roll = self.char_armor.armor.armor_roll(self.char_id_race)
        char_armor_total = char_armor_roll[2] +  + char_att['DEF']

        char_stamina_roll = self.char_stamina.stamina.stamina_roll(self.char_id_race)
        char_stamina_total = char_stamina_roll[2]
    
        print(f"{self.char_name}, você é um(a) {self.char_race_name} {self.char_class_name}, portanto sua vida inicial é de {char_hp_roll[0]}.\nO dado rolado para seu atributo de vida '{id_att['HLN']['att_name']}' caiu em {char_att_rolls['HLN']}, totalizando ele para {id_att['HLN']['att_value']}, e o dado rolado para aumento de vida caiu em {char_hp_roll[1]}, portanto sua vida máxima é {char_max_hp}.\nVocê possui armadura inicial de {char_armor_roll[0]}. O dado rolado para seu atributo de defesa '{id_att['DEF']['att_name']}' caiu em {char_att_rolls['DEF']}, totalizando ele para {id_att['DEF']['att_value']}, e o dado rolado para aumento de armadura caiu em {char_armor_roll[1]}, portanto sua armadura é {char_armor_total}, que protejerá contra ataques iguais ou menores que o valor dela.\nSeus pontos iniciais de vigor são {char_stamina_roll[0]} e o dado rolado caiu em {char_stamina_roll[1]}, totalizando seus pontos de vigor para {char_stamina_total}.")

character = Character()

if __name__ == '__main__':
    character.character_selection()
    character.character_points()