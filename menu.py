import os
os.system("cls")

def mostrar_opções():
    print("Escolha uma das opções abaixo [1 a 6]: ")
    print("1 - Adicionar Treino ")
    print("2 - Vizualizar Treinos ")
    print("3 - Atualizar Treino ")
    print("4 - Deletar Treino ")
    print("5 - Filtrar Treinos ")
    print("6 -  Metas... ")
    print("7 - SAIR ")
    
def mostrar_opções_metas():
    print("Escolha uma das opções abaixo [1 a 4]: ")
    print("1 - Adicionar Meta ")
    print("2 - Vizualizar Metas ")
    print("3 - Atualizar Meta ")
    print("4 - Deletar Meta ")
    print("5 - SAIR ")

def main():
    import treinos_delete
    import treinos_filter
    import treinos_insert
    import treinos_update
    import treinos_view
    while True:
        mostrar_opções()
        try:
            opcao=int(input())
        except ValueError:
            print("Tente digitando um numero acima [1 a 8]")
        if opcao==1:
            treinos_insert.adicionar_treino()

        elif opcao==2:
            treinos_view.vizualizar_treinos()

        elif opcao==3:
            treinos_update.treino_atualizar()

        elif opcao==4:
            treinos_delete.deletar_treino()
        
        elif opcao==5:
            treinos_filter.menu_filtragem()

        elif opcao==6:
            mostrar_opções_metas()

        elif opcao==7:
            print("Fechando Programa...")
            break

if __name__=="__main__":
    main()