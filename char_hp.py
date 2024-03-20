class CharHP:

    def __init__(self):

        import random
        self.random = random

        from char_race import race_human, race_elf, race_dwarf, race_orc, race_animana

        self.race_human = race_human
        self.race_elf = race_elf
        self.race_dwarf = race_dwarf
        self.race_orc = race_orc
        self.race_animana = race_animana

    def hp_roll(self, id_race):
        if id_race == 0:
            initial_hp = self.race_human['initial_stats_race']['race_initial_hp']
            roll_hp = self.random.randint(10, 20)
            calc_hp = initial_hp + roll_hp
            return initial_hp, roll_hp, calc_hp
        elif id_race == 1:
            initial_hp = self.race_elf['initial_stats_race']['race_initial_hp']
            roll_hp = self.random.randint(10, 20)
            calc_hp = initial_hp + roll_hp
            return initial_hp, roll_hp, calc_hp
        elif id_race == 2:
            initial_hp = self.race_dwarf['initial_stats_race']['race_initial_hp']
            roll_hp = self.random.randint(10, 20)
            calc_hp = initial_hp + roll_hp
            return initial_hp, roll_hp, calc_hp
        elif id_race == 3:
            initial_hp = self.race_orc['initial_stats_race']['race_initial_hp']
            roll_hp = self.random.randint(10, 20)
            calc_hp = initial_hp + roll_hp
            return initial_hp, roll_hp, calc_hp
        elif id_race == 4:
            initial_hp = self.race_animana['initial_stats_race']['race_initial_hp']
            roll_hp = self.random.randint(10, 20)
            calc_hp = initial_hp + roll_hp
            return initial_hp, roll_hp, calc_hp
        
hp = CharHP()

if __name__ == "__main__":
    print(hp.hp_roll(0))
    print(hp.hp_roll(1))
    print(hp.hp_roll(2))
    print(hp.hp_roll(3))
    print(hp.hp_roll(4))