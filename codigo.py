def funcao(opcao):
    if opcao == 'E':
        funcionalidade = input("""
como deseja ver as receitas?
tudo
por país
favoritos
aleatório""")

    elif opcao == 'a':
        print("ir para 'alterar'")    
    
    
    return

while True:
    opcao = input("""
Exibir -------> E
Alterar ------> A                  

Digite a funcionalidade desejada: """)
    
    if opcao == "stop":
        break
    
    else:
        funcao(opcao)

