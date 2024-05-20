import random

def exebir_tudo():
    file = open("tudo.txt", "r")
    print(file.read())
    file.close()
    return

def exebir_por_pais():
    pais = input("digite o pais do qual deseja ver as receitas: ")
            
    file = open("tudo.txt", "r")
            
    for linha in file:
        if f"{pais}|" in linha:
            print(linha)
    file.close()        
    return

def exebir_favoritos():
    file = open("favoritos.txt", "r")
    print(file.read())
    file.close()
    return

def exebir_aleatorio():
    file = open("tudo.txt", "r")
            
    ret = []
    for linha in file:
        ret.append(linha)
                
    aleatorio = random.randint(0, len(ret)-1)
            
    print(ret[aleatorio])
    file.close()
    return

def alterar_adicionar():
    pais = input("Digite o país de origem da nova receita: ")
    nome = input("Digite o nome da receita: ")
    preparo = input("Digite o preparo da receita com os ingredientes: ")
    novareceita = (f"{pais}|{nome}|{preparo}\n")
            
    file = open("tudo.txt", "a")
    file.write(novareceita)
    file.close()
    
    favoritos = input("""
deseja adicionar a receita aos favoritos?
[1] sim
[2] não
""")
    
    continuar = input("""
deseja continuar adicionando? 
[1] sim
[2] não
""")

    if continuar == "1":
        alterar_adicionar()

    elif continuar == "2":
        print("========================================================")        
            
    if favoritos == "1":
        file = open("favoritos.txt", "a")
        file.write(novareceita)
        file.close()    
    return

def alterar_remover():
    receita = input ("Digite o nome da receita que irá ser removida: ")
            
    file = open("tudo.txt", "r")
    linhas = file.readlines()
    file.close()
            
    file_remover = open("tudo.txt", "w")
    for linha in linhas:
        if f";{receita};" not in linha:
            file_remover.write(linha)

    file_remover.close()

    file = open("favoritos.txt", "r")
    linhas = file.readlines()
    file.close()

    file_remover = open("favoritos.txt", "w")
    for linha in linhas:
        if receita not in linha:
            file_remover.write(linha)
            
    file_remover.close()                         
    return

  
while True:
    opcao = input("""
Exibir -------> E
Alterar ------> A
Encerrar -----> X                  

Digite a funcionalidade desejada: """)
    
    if opcao == "E" or opcao == "e":
        funcionalidade_exibir = input("""                            
Como deseja exebir as receitas?
[1] Tudo 
[2] Por país 
[3] Favoritos 
[4] Aleatório
[X] Voltar
""")
        if funcionalidade_exibir == "1":
            exebir_tudo()

        elif funcionalidade_exibir == "2":
            exebir_por_pais()

        elif funcionalidade_exibir == "3":
            exebir_favoritos()  

        elif funcionalidade_exibir == "4":
            exebir_aleatorio()

        elif funcionalidade_exibir == "X" or funcionalidade_exibir == "x":
            print("========================================================")        

    elif opcao == "A" or opcao == "a":
        funcionalidade_alterar = input("""
Como deseja deseja alterar uma receita?
[1] Adicionar 
[2] Remover 
[3] Editar
[X] Voltar
""" )
        if funcionalidade_alterar == "1":
            alterar_adicionar()

        elif funcionalidade_alterar == "2":
            alterar_remover()

        elif funcionalidade_alterar == "X" or funcionalidade_alterar == "x":
            print("========================================================")        

    elif opcao == "X" or opcao == "x":
        break

    else:
        print("opção inválida")
            