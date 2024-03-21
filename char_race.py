class CharRace:

    def __init__(self):
        self.races = []
        self.race_next_id = 0

    def race_creation(self, race_name, race_values):
        race_id = self.race_next_id
        race_initial_stats = dict(zip(["race_initial_hp", "race_initial_stamina", "race_initial_armor", "race_initial_points"], race_values))
        new_race = {'id_race': race_id, 'name_race': race_name, 'initial_stats_race': race_initial_stats}
        self.races.append(new_race)
        races_id_name[race_id] = race_name
        self.race_next_id += 1
        return new_race
    
    def race_selection(self):
        while True:

            print("Opções de raças:")
            for race_id, race_name in races_id_name.items():
                print(f"{race_id} - {race_name}")
            
            try:
                char_id_race = int(input("Escolha digitando o respectivo número da raça: "))
            except ValueError:
                print("Entrada inválida. Por favor, insira um número.")
                continue
            
            if char_id_race in races_id_name:
                char_id_race_confirm = str(input(f"Você escolheu '{races_id_name[char_id_race]}'.\nTem certeza que deseja prosseguir? (S / N) ").upper())
                if char_id_race_confirm == 'S':
                    print(f"Sua raça é '{races_id_name[char_id_race]}'.")
                    return char_id_race
                else:
                    print("Escolha cancelada.")
            else:
                print("Número de raça inexistente ou inválido. Tente novamente.")

race = CharRace()

races_id_name = {}

race_human = race.race_creation("Humano", [70, 5, 0, 3])
race_elf = race.race_creation("Elfo", (60, 5, 0, 3))
race_dwarf = race.race_creation("Anão", (90, 5, 0, 3))
race_orc = race.race_creation("Orc", (120, 5, 0, 1))
race_animana = race.race_creation("Animana", (50, 5, 0, 4))

if __name__ == "__main__":
    print(race.races[0])