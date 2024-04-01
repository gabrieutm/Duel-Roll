import random
#from char_skill_effect import charskilleffect

class SkillSpecial:

    def __init__(self):
        self.skill_spc_cost = 5
        self.skill_spc_cooldown = 3
        self.skill_spc_cooldown_on = False
        self.skill_next_id = 0
        self.skills_spc = []



    def skill_spc_creation(self, skill_class, skill_name, skill_att_groups, skill_details):
        skill_id = self.skill_next_id
        
        skill_info = dict(zip(['skill_desc', 'skill_effect_desc', 'skill_effect', 'skill_roll'], skill_details))
        
        new_skill = {'id_skill': skill_id, 'class_skill': skill_class, 'name_skill': skill_name, 'att_groups_skill': skill_att_groups, 'info_skill': skill_info}
        
        self.skills_spc.append(new_skill)
        self.skill_next_id += 1
        return new_skill



    def skill_spc_effect(self):
        pass
    


    def skill_spc(self, player, enemy, characters, menu): #deixar pra fazer depois que criar os spc

        class_skills = []
        
        for skills in skillspc.skills_spc:
        
            for skill_values in skills.values():
                
                if skill_values == characters[player]['class']:

                    class_skills.append(skills)
        
        class_skills = {index: skill for index, skill in enumerate(class_skills)}

        while True:

            for key, skill in class_skills.items():
                print(f"{key} - {skill['name_skill']}\n{skill['info_skill']['skill_desc']}")
                
            choose_skill = input("Digite o respectivo número da habilidade que deseja utilizar: (ou digite 'voltar')").lower()
            
            try:

                if choose_skill == 'voltar':

                    menu(player, enemy)
                    break

                elif int(choose_skill) in class_skills.keys():

                    chosen_skill = class_skills[int(choose_skill)]

                    chosen_skill_confirm = input(f"Tem certeza que deseja usar a habilidade {chosen_skill['name_skill']}? (S/N) ").upper()
            
                    if chosen_skill_confirm == 'S':

                        roll_hit = random.randint(1, 20)

                        if roll_hit > characters[enemy]['current_armor']:
                            print('ok')

                        #vou precisar criar uma função pra cada especial e colocar todas as funções num unico dicionario acessível pelo nome da habilidade, são muito diferentes
                        
                        else:
                            print(f"Dado: {roll_hit}.\nVocê errou! (armadura do oponente: {characters[enemy]['current_armor']})")
                            break

                    else:
                        continue
                
                else:
                    print("Entrada inválida. Por favor, insira um número da lista.")
                    continue
            
            except:
                print("Entrada inválida. Por favor, insira um número da lista.")
                continue



skillspc = SkillSpecial()



skillspc_genesis_overload = skillspc.skill_spc_creation('Mago', 'Sobrecarga Gênesis', ['ATK'], ('O mago evoca uma aura de energia primordial que envolve o ambiente ao redor do oponente. Neste vórtice do início de toda a magia, a própria essência do inimigo é sobrecarregada, levando à desintegração de sua existência.', 'Se atingido, este ataque especial atordoa o oponente por um turno. Até que ele realize uma ação, seus atributos são reduzidos de acordo com os atributos do mago.', None, random.randint(1, 12)))



skillspc_berserker_extermination = skillspc.skill_spc_creation('Bárbaro', 'Extermínio Berserker', ['ATK','DEF'], ('O bárbaro se fortifica e desencadeia um frenesi de ataques selvagens e implacáveis, aniquilando seu oponente com uma ferocidade monstruosa.', 'Se atingido, este ataque especial duplica seu valor de ataque e defesa por um turno, e você pode realizar uma ação adicional nesse mesmo turno.', None, random.randint(1, 12)))



skillspc_marked_to_death = skillspc.skill_spc_creation('Assassino', 'Marcado Para Morrer', ['ATK'], ('O assassino fica entorpecido por um instinto sanguinário e utiliza de todas as suas habilidades contra o oponente.', 'Este ataque possui vantagem para ser acertado (mesmo que você esteja afetado pela desvantagem), e caso atingido, causa dano ao oponente e ainda ativa o efeito de todas as suas outras habilidades.', None, random.randint(1, 12)))


skillspc_the_devils_fear = skillspc.skill_spc_creation('Necromante', 'O Medo do Diabo', ['ATK'], ('O necromante revela sua verdadeira forma, envolvendo seu alvo em um abraço gélido de terror, enquanto sombras macabras dilaceram seu ser.', 'Se atingido, o dano do seu próximo ataque é maximizado e também é duplicado, e o inimigo tem desvantagem para atacar você por um turno', None, random.randint(1, 12)))



skillspc_voodoo_doll = skillspc.skill_spc_creation('Bruxa', 'Boneca de Voodoo', ['DEF','HLN'], ('A bruxa se envolve em um véu sombrio que a transforma em um reflexo vivo de seu oponente.', 'Por um turno, todo dano e efeitos recebidos são redirecionados para o oponente e metade do dano é direcionado como cura para a bruxa. Durante esse tempo, a bruxa tem 0 de armadura, podendo acertar a si mesma para causar metade do dano do ataque utilizado.', None, 0))



if __name__ == '__main__':
    pass