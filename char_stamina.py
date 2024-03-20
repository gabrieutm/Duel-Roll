class CharStamina:

    def __init__(self):

        import random
        self.random = random

        from char_race import race_human, race_elf, race_dwarf, race_orc, race_animana

        self.race_human = race_human
        self.race_elf = race_elf
        self.race_dwarf = race_dwarf
        self.race_orc = race_orc
        self.race_animana = race_animana

    def stamina_roll(self, id_race):
        if id_race == 0:
            initial_stamina = self.race_human['initial_stats_race']['race_initial_stamina']
            roll_stamina = self.random.randint(1, 4)
            calc_stamina = initial_stamina + roll_stamina
            return initial_stamina, roll_stamina, calc_stamina
        elif id_race == 1:
            initial_stamina = self.race_elf['initial_stats_race']['race_initial_stamina']
            roll_stamina = self.random.randint(1, 4)
            calc_stamina = initial_stamina + roll_stamina
            return initial_stamina, roll_stamina, calc_stamina
        elif id_race == 2:
            initial_stamina = self.race_dwarf['initial_stats_race']['race_initial_stamina']
            roll_stamina = self.random.randint(1, 4)
            calc_stamina = initial_stamina + roll_stamina
            return initial_stamina, roll_stamina, calc_stamina
        elif id_race == 3:
            initial_stamina = self.race_orc['initial_stats_race']['race_initial_stamina']
            roll_stamina = self.random.randint(1, 4)
            calc_stamina = initial_stamina + roll_stamina
            return initial_stamina, roll_stamina, calc_stamina
        elif id_race == 4:
            initial_stamina = self.race_animana['initial_stats_race']['race_initial_stamina']
            roll_stamina = self.random.randint(1, 4)
            calc_stamina = initial_stamina + roll_stamina
            return initial_stamina, roll_stamina, calc_stamina

stamina = CharStamina()

if __name__ == '__main__':
    print(stamina.stamina_roll(1))