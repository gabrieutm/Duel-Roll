class CharArmor:

    def __init__(self):

        import random
        self.random = random

        from char_race import race_human, race_elf, race_dwarf, race_orc, race_animana
        self.race_human = race_human
        self.race_elf = race_elf
        self.race_dwarf = race_dwarf
        self.race_orc = race_orc
        self.race_animana = race_animana

    def armor_roll(self, id_race):
        if id_race == 0:
            initial_armor = self.race_human['initial_stats_race']['race_initial_armor']
            roll_armor = self.random.randint(5, 10)
            calc_armor = initial_armor + roll_armor
            return initial_armor, roll_armor, calc_armor
        elif id_race == 1:
            initial_armor = self.race_elf['initial_stats_race']['race_initial_armor']
            roll_armor = self.random.randint(5, 10)
            calc_armor = initial_armor + roll_armor
            return initial_armor, roll_armor, calc_armor
        elif id_race == 2:
            initial_armor = self.race_dwarf['initial_stats_race']['race_initial_armor']
            roll_armor = self.random.randint(5, 10)
            calc_armor = initial_armor + roll_armor
            return initial_armor, roll_armor, calc_armor
        elif id_race == 3:
            initial_armor = self.race_orc['initial_stats_race']['race_initial_armor']
            roll_armor = self.random.randint(5, 10)
            calc_armor = initial_armor + roll_armor
            return initial_armor, roll_armor, calc_armor
        elif id_race == 4:
            initial_armor = self.race_animana['initial_stats_race']['race_initial_armor']
            roll_armor = self.random.randint(5, 10)
            calc_armor = initial_armor + roll_armor
            return initial_armor, roll_armor, calc_armor
    
armor = CharArmor()

if __name__ == '__main__':
    print(armor.armor_roll(0))