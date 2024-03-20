class CharClass:

    def __init__(self):
        self.classes = []
        self.class_next_id = 0
    
    def class_creation(self, class_name, class_values):
        class_id = self.class_next_id
        class_initial_stats = dict(zip(["num_skill_atk", "num_skill_hln", "num_skill_def"], class_values))
        new_class = {'id_class': class_id, 'name_class': class_name, 'initial_stats_class': class_initial_stats}
        self.classes.append(new_class)
        classes_id_name[class_id] = class_name
        self.class_next_id += 1
        return new_class
    
    def class_selection(self):
        while True:

            print("Opções de classe:")
            for class_id, class_name in classes_id_name.items():
                print(f"{class_id} - {class_name}")
            
            try:
                char_id_class = int(input("Escolha digitando o respectivo número da classe: "))
            except ValueError:
                print("Entrada inválida. Por favor, insira um número.")
                continue
            
            if char_id_class in classes_id_name:
                char_id_class_confirm = str(input(f"Você escolheu '{classes_id_name[char_id_class]}'.\nTem certeza que deseja prosseguir? (S / N)").upper())
                if char_id_class_confirm == 'S':
                    print(f"Sua classe é '{classes_id_name[char_id_class]}'.")
                    return char_id_class
                else:
                    print("Escolha cancelada.")
            else:
                print("Número de classe inexistente ou inválido. Tente novamente.")

classs = CharClass()

classes_id_name = {}

class_mage = classs.class_creation("Mago", (2, 1, 1))
class_barbarian = classs.class_creation("Bárbaro", (2, 1, 1))
class_assassin = classs.class_creation("Assassino", (2, 1, 1))
class_necromancer = classs.class_creation("Necromante", (2, 1, 1))
class_witch = classs.class_creation("Bruxa", (2, 1, 1))

if __name__ == "__main__":
    print(classs.classes)