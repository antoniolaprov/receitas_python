<<<<<<< HEAD
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
=======
def titulo_cardapio(txt):
    print(('-'*30))
    print(txt)
    print(('-'*30))


def adicionar_receita():
    print("Opção 1 - Adicionar Receita")

def visualizar_receitas():
    print("Opção 2 - Visualizar Receitas")


def atualizar_receitas():
    print("Opção 3 - Atualizar receitas")

def excluir_receitas():
    print("Opção 4 - Excluir Receitas")

def filtrar_por_pais():
    print("Opção 5 - Filtrar por País")   

def lista_de_favoritos():
    print("Opção 6 - Lista de Favoritos")
>>>>>>> 8303e90c5d55fe3a0bf7dc18e9c20decccacc3aa
    
    
    return

while True:
    opcao = input("""
mostrar -------> m
alterar -------> a                  

<<<<<<< HEAD
Digite a funcionalidade desejada: """)
    
    if opcao == "stop":
        break
    
    else:
        funcao(opcao)

=======
def main():
    titulo_cardapio("CARDAPIO DE RECEITAS")

    while True:
        print("""Escolha uma opção:
1 - Adicionar Receita
2 - Visualizar Receitas
3 - Atualizar Receitas
4 - Excluir Receitas
5 - Filtrar por País
6 - Lista de Favoritos
7 - Sugestão de Receita Aleatória
8 - Pesquisar por Ingredientes
9 - Sair
Digite o número da opção desejada:""")
        
        opcao = input()  

        if opcao == '1':
            adicionar_receita()
        elif opcao == '2':
            visualizar_receitas()
        elif opcao == '3':
            atualizar_receitas()
        elif opcao == '4':
            excluir_receitas()
        elif opcao == '5':
            filtrar_por_pais()
        elif opcao == '6':
            lista_de_favoritos()
        elif opcao == '7':
            sugestao_receita_aleatoria()
        elif opcao == '8':
            pesquisar_por_ingredientes()
        elif opcao == '9':
            sair()
        else:
            print("Opção inválida. Digite um número de 1 a 9.")

main()
>>>>>>> 8303e90c5d55fe3a0bf7dc18e9c20decccacc3aa
