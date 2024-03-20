class CharAttribute: 

    def __init__(self):

        import random
        self.random = random

        self.attributes = []
        self.attributes_next_id = 0
    
    def att_creation(self, att_values):
        attribute_id = self.attributes_next_id
        att_group = dict(zip(["att_name", "att_nick", "att_value", "att_mod", "att_max", "att_min"], att_values))
        new_attribute = {"id_attribute": attribute_id, "ATK": dict(zip(att_group, att_values[:6])), "HLN": dict(zip(att_group, att_values[6:12])), "DEF": dict(zip(att_group, att_values[12:]))}
        self.attributes.append(new_attribute)
        attributes_id_name[attribute_id] = att_values[0]
        attributes_id_nick[attribute_id] = att_values[1]
        self.attributes_next_id += 1
        return new_attribute
    
    def att_roll(self):
        att_rolls = {}
        for group in attributes_groups:
            att_rolls[group] = self.random.randint(1, 6)
        return att_rolls

    def att_mod_value(self, attribute_id, att_group, att_up_down, att_dif_value):
        for attribute in self.attributes:
            if attribute['id_attribute'] == attribute_id and att_group in attribute:
                if att_up_down == "U":
                    attribute[att_group]['att_value'] += att_dif_value
                    attribute[att_group]['att_mod'] = att_dif_value
                elif att_up_down == "D":
                    attribute[att_group]['att_value'] -= att_dif_value
                    attribute[att_group]['att_mod'] = -att_dif_value
                break

attribute = CharAttribute()

attributes_groups = ("ATK", "DEF", "HLN")
attributes_id_name = {}
attributes_id_nick = {}

atts_mage = attribute.att_creation(("MANA", "MAN", 0, 0, 20, -5, "CONHECIMENTO", "CNT", 0, 0, 20, -5, "CONSTITUIÇÃO", "CON", 0, 0, 20, -5))
atts_babarian = attribute.att_creation(("FORÇA", "FOR", 0, 0, 20, -5, "DUREZA", "DUR", 0, 0, 20, -5, "CONSTITUIÇÃO", "CON", 0, 0, 20, -5))
atts_assassin = attribute.att_creation(("DESTREZA", "DES", 0, 0, 20, -5, "ASTÚCIA", "AST", 0, 0, 20, -5, "CONSTITUIÇÃO", "CON", 0, 0, 20, -5))
atts_necromancer = attribute.att_creation(("ESPÍRITO", "ESP", 0, 0, 20, -5, "VONTADE", "VON", 0, 0, 20, -5, "CONSTITUIÇÃO", "CON", 0, 0, 20, -5))
atts_witch = attribute.att_creation(("MALÍCIA", "MAL", 0, 0, 20, -5, "ERAS", "ERA", 0, 0, 20, -5, "CONSTITUIÇÃO", "CON", 0, 0, 20, -5))

#attribute.att_mod_value(1, "ATK", "U", 5)

if __name__ == "__main__":
    print(attribute.attributes)
    print(attribute.att_roll())