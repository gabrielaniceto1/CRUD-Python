import os
os.system("cls")

def mostrar_metas():
    with open("csv\Metas.csv","r") as file:
        for i in file:
            linha=i.split(",")
            print(f"Meta: {linha[0]} | Tempo desejado: {linha[1]} | Distancia desejada: {linha[2]}")

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
    print("2 - Atualizar Meta ")
    print("3 - Deletar Meta ")
    print("4 - SAIR ")

def main():
    import treinos_delete
    import treinos_filter
    import treinos_insert
    import treinos_update
    import treinos_view
    import treino_goals
    while True:
        mostrar_metas()
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
            while True:
                mostrar_opções_metas()
                opcao2=input()
                if opcao2=="1":
                    treino_goals.adicionar_meta()
                elif opcao2=="2":
                    treino_goals.atualizar_meta()
                elif opcao2=="3":
                    treino_goals.deletar_meta()
                elif opcao2=="4":
                    print("Saindo...")
                    break
                else:
                    print("Tente novamente um dos numeros acima!")


        elif opcao==7:
            print("Fechando Programa...")
            break

if __name__=="__main__":
    main()