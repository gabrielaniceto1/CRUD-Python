import csv
import os
os.system("cls")

def adicionar_treino():
    nome=str(input("Digite o nome do treino/competição: ")).capitalize()
    data=str(input("Digite a data do treino/competição: "))
    while True:
        try:
            tempo=float(input("Digite (em minutos) a duração do seu treino/competição: "))
            distancia=float(input("Digite (em km) a distancia percorrida: "))
            break
        except ValueError:
            print("Digite em numeros")
    local=str(input("Digite o local do seu treino/competição: ")).capitalize()
    clima=str(input("Digite o clima do local: ")).capitalize()

    treino=(f"{nome},{data},{str(tempo)},{str(distancia)},{local},{clima}")
    with open("Treinos.csv","a", encoding="utf8") as file:
        file.write(treino)

if __name__=="__main__":
    adicionar_treino()