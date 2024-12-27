import csv
import os
os.system("cls")

def adicionar_treino():
    with open("csv\Treinos.csv","r", encoding="utf8") as file:
        lista=file.readlines()
    nome=str(input("Digite o nome do treino/competição: ")).upper()
    data=str(input("Digite a data do treino/competição: "))
    while True:
        try:
            tempo=float(input("Digite (em minutos) a duração do seu treino/competição: "))
            distancia=float(input("Digite (em km) a distancia percorrida: "))
            break
        except ValueError:
            print("Digite em numeros")
    local=str(input("Digite o local do seu treino/competição: ")).upper()
    clima=str(input("Digite o clima do local: ")).upper()

    treino=(f"{nome},{data},{str(tempo)},{str(distancia)},{local},{clima}")
    with open("csv\Treinos.csv","a", encoding="utf8") as file:
        if len(lista)<=0:
            file.write(treino)
        else:
            file.write(f"\n{treino}")
    print("Treino adicionado como sucesso!")
    import os
    sair=input("Digite ENTER para sair ")
    os.system("cls")
if __name__=="__main__":
    adicionar_treino()