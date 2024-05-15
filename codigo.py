def funcao(opcao):
    if opcao == 'm':
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
mostrar -------> m
alterar -------> a                  

Digite a funcionalidade desejada: """)
    
    if opcao == "stop":
        break
    
    else:
        funcao(opcao)

