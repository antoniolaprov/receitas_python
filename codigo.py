def adicionar_receita():
    print("Opção 1 - Adicionar Receita")

def visualizar_receitas():
    print("Opção 2 - Visualizar Receitas")

def atualizar_receitas():
    print("Opção 3 - Atualizar Receitas")

def excluir_receitas():
    print("Opção 4 - Excluir Receitas")

def filtrar_por_pais():
    print("Opção 5 - Filtrar por País")   

def lista_de_favoritos():
    print("Opção 6 - Lista de Favoritos")
    
def sugestao_receita_aleatoria():
    print("Opção 7 - Sugestão de Receita Aleatória")
    
def pesquisar_por_ingredientes():
    print("Opção 8 - Pesquisar por Ingredientes")

def sair():
    print("Opção 9 - Sair")
    print("Saindo do programa...")
    exit()

def main():
    while True:
        print("Escolha uma opção:")
        print("1 - Adicionar Receita")
        print("2 - Visualizar Receitas")
        print("3 - Atualizar Receitas")
        print("4 - Excluir Receitas")
        print("5 - Filtrar por País")
        print("6 - Lista de Favoritos")
        print("7 - Sugestão de Receita Aleatória")
        print("8 - Pesquisar por Ingredientes")
        print("9 - Sair")

        opcao = input("Digite o número da opção desejada: ")

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
print('teste')