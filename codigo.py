def titulo():
    print('='*30)
    print("MANUAL DE RECEITAS")
    print('='*30)



def funcao(opcao):
    if opcao == 'E' or opcao == 'e':
        funcionalidade_exibir = input("""                            
Como deseja ver as receitas?
[1] Tudo 
[2] Por país 
[3] Favoritos 
[4] Aleatório
""" )
        if funcionalidade_exibir == "1":
            print(f"{novareceita}")
            return receita
        elif funcionalidade_exibir == "2":
            print(f"{pais},{nome}")
            return
        elif funcionalidade_exibir == "3":
            print("'Exibir Favoritos' ainda não implementada.")
        elif funcionalidade_exibir == "4":
            print(" 'Exibir Aleatório' ainda não implementada.")
        else:
            print("Opção inválida.")
    
    elif opcao == 'A' or opcao == "a":
        funcionalidade_alterar = input("""
Como deseja deseja alterar uma receita?
[1] Adicionar 
[2] Remover 
[3] Editar 
""" )
        if funcionalidade_alterar == "1":
            pais = input("Digite o país de origem da nova receita: ")
            nome = input("Digite o nome da nova receita: ")
            preparo = input("Digite o preparo da receita com os ingredientes: ")
            novareceita = (f"{pais};{nome};{preparo} \n")
            return print(novareceita)
        elif  funcionalidade_alterar == "2":
            receita = input ("Digite o nome da receita que irá ser removida: ")
            return receita
        elif funcionalidade_alterar == "3":
            receita = input("Digite a receita que irá ser editada: ")
            return receita


titulo()
while True:
    opcao = input("""
Exibir -------> E
Alterar ------> A                  

Digite a funcionalidade desejada: """)
    
    if opcao == "stop":
        break
    else:
        funcao(opcao)

