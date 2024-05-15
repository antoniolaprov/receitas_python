def funcao(opcao):
    if opcao == 'm':
        print("ir para 'mostrar'")

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

